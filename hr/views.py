from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import *
from assets.models import Asset
from .filters import *
from .forms import StaffForm, ContractForm, PositionForm, SignatureForm

import django_tables2 as tables
from django_tables2.utils import A
from jsignature.utils import draw_signature


# Tables


class StaffTable(tables.Table):
    pos = tables.Column(accessor='position.title')
    link = tables.LinkColumn(
        'staff_view',
        args=[A('pk')],
        orderable=False,
        text='View'
    )

    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'staff_type']
        attrs = {'class': 'paleblue'}


# Views

@login_required
def index(request):
    if request.user.has_perm('hr_access'):
        contracts = Contract.objects.all()
        x = 0
        for c in contracts:
            if c.ending_soon() == True:
                x += 1
        if x >0:
            messages.warning(request, '%i contracts are about to expire.' % x)

    return render(request, 'hr/index.html', {})


@login_required
def contact_list(request):
    # searchable list of contacts
    pass


@login_required
def staff_profile(request):
    pass


@login_required
def staff_list(request):
    staff = Staff.objects.all()
    table = StaffTable(staff)
    f = StaffFilter(request.GET, queryset=Staff.objects.all())
    return render(
        request,
        'hr/staff_list.html',
        {'table': table, 'staff': staff, 'f': f}
    )


@login_required
def staff_view(request, staff_id):
    context_dict = {}
    s = Staff.objects.get(id=staff_id)
    p = s.get_position()
    assets = Asset.objects.all()
    print assets
    myassets = [a for a in assets if a.assigned() == s ]
    print myassets

    try:
        c = Contract.objects.filter(staff_id=staff_id).order_by('-start_date')
    except:
        c = None

    context_dict['staff'] = s
    context_dict['position'] = p
    context_dict['contract_set'] = c
    context_dict['asset_list'] = myassets
    context_dict['countryflag'] = s.nationality.__unicode__().lower()
    return render(request, 'hr/staff_view.html', context_dict)


class StaffCreate(CreateView):
    template_name = 'hr/generic_form.html'
    form_class = StaffForm
    # success_url = '/hr/staff'


class ContractCreate(CreateView):
    template_name = 'hr/generic_form.html'
    form_class = ContractForm
    success_url = '/hr/staff'


class PositionCreate(CreateView):
    template_name = 'hr/generic_form.html'
    form_class = PositionForm
    success_url = '/hr/staff'

class SignatureCreate(CreateView):
    template_name = 'hr/signature_form.html'
    form_class = SignatureForm
    success_url = '/hr/staff'


class StaffUpdate(UpdateView):
    model = Staff
    form_class = StaffForm


class PositionUpdate(UpdateView):
    model = Position
    form_class = PositionForm


class ContractUpdate(UpdateView):
    model = Contract
    form_class = ContractForm


class PositionView(DetailView):
    model = Position
    template_name = 'hr/position_view.html'


class ContractView(DetailView):
    model = Contract
    template_name = 'hr/contract_view.html'


class SignatureView(DetailView):
    model = JSignatureModel
    template_name = 'hr/signature_view.html'


@login_required
def view_signature(request):
    print request.POST
    form = SignatureForm(request.POST or None)
    print form
    if form.is_valid():
        print 'valid form'
        print form.cleaned_data.get('signature')
        signature = form.cleaned_data.get('signature')
        if signature:
            print 'signature found'
            # as an image
            signature_picture = draw_signature(signature)
            print signature_picture
            j = JSignatureModel()
            j.signature = signature
            j.save()

            return render(
                request,
                'hr/signature_form.html',
                {
                    'signature': signature,
                    'form': form
                }
            )
    print 'form not valid'
    return render(
        request,
        'hr/signature_form.html',
        {
            'form': form
        }
    )


def test_signature(request):
    return render(request, 'hr/signature_form.html', {})
