from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .filters import *
from .forms import StaffForm, ContractForm, PositionForm
import django_tables2 as tables
from django_tables2.utils import A


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
    messages.warning(request, "There are X contracts marked for review that are about to expire")
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
    try:
        c = Contract.objects.filter(staff_id=staff_id).order_by('-start_date')
    except:
        c = None

    context_dict['staff'] = s
    context_dict['position'] = p
    context_dict['contract_set'] = c
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
