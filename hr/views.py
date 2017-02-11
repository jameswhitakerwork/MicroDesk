from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
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
    p = Position.objects.get(staff_id=staff_id)
    try:
        c = Contract.objects.filter(staff_id=staff_id).order_by('-start_date')
    except:
        c = None

    context_dict['staff'] = s
    context_dict['position'] = p
    context_dict['contract_set'] = c
    context_dict['countryflag'] = s.nationality.__unicode__().lower()
    return render(request, 'hr/staff_view.html', context_dict)


def staff_form(request):
    # if this is a post request, process the form data
    if request.method == 'POST':
        # create form and populate it with request
        form = StaffForm(request.POST)
        # check whether form is valid
        if form.is_valid():
            # process data in form.cleaned_data
            # redirect to url
            return render(request, 'hr/staff_list.html', {})
    # if a GET, create blank form
    else:
        form = StaffForm()

    return render(request, 'hr/generic_form.html', {'form': form})


class ContractView(FormView):
    template_name = 'hr/generic_form.html'
    form_class = ContractForm
    success_url = '/hr/staff_list'

    def form_valid(self):
        # when valid form is posted
        print 'contract added'
        return super(ContractView, self).form_valid(form)

class PositionView(FormView):
    template_name = 'hr/generic_form.html'
    form_class = PositionForm
    success_url = '/hr/staff_list'

    def form_valid(self):
        # when valid form is posted
        print 'position added'
        return super(ContractView, self).form_valid(form)
