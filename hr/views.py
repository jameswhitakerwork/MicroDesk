from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import *
import django_tables2 as tables
from django_tables2.utils import A
# Tables


class StaffTable(tables.Table):
    Link = tables.LinkColumn(
        'staff_view',
        args=[A('pk')],
        orderable=False,
        text='View'
    )

    class Meta:
        model = Staff
        fields = ['first_name', 'last_name']
        attrs = {'class': 'paleblue'}

# Views


def index(request):
    messages.success(request, "You are logged in!")
    messages.warning(request, "But this app is not ready yet...")
    return render(request, 'hr/index.html', {})


def contact_list(request):
    # searchable list of contacts
    pass


def staff_profile(request):
    pass


def staff_list(request):
    staff = Staff.objects.all()
    table = StaffTable(staff)
    return render(request, 'hr/staff_list.html', {'table': table})


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
