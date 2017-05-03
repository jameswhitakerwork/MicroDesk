from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .forms import Checkin_Form, Checkout_Form, AssetForm
from .filters import AssetFilter
import django_tables2 as tables
from django_tables2.utils import A
from jsignature.utils import draw_signature
from django.forms.models import inlineformset_factory
import csv

# Create your views here.


class Asset_Create(CreateView):
    form_class = AssetForm
    template_name = "hr/generic_form.html"
    success_url = "/assets/asset-list.html"


class Asset_View(DetailView):
    model = Asset
    template_name = 'assets/asset_view.html'


    def get_context_data(self, **kwargs):
        ctx = super(Asset_View, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        checks = Check.objects.filter(asset=pk)
        ctx['checks'] = checks
        return ctx



class Checkout_Create(CreateView):
    form_class = Checkout_Form
    template_name = "assets/checkout_form.html"
    success_url = "/"

    def get_initial(self):
        try:
            a = self.kwargs['asset_id']
        except:
            a = None
        return {'asset': a, 'check_type': 'out'}

    def get_context_data(self, **kwargs):
        ctx = super(Checkout_Create, self).get_context_data(**kwargs)
        asset_id = self.kwargs['asset_id']
        ctx['asset'] = Asset.objects.get(id=asset_id)
        return ctx


class Checkin_Create(CreateView):
    form_class = Checkin_Form
    template_name = "assets/checkin_form.html"
    success_url = "/"

    def get_initial(self):
        try:
            a = self.kwargs['asset_id']
        except:
            a = None
        asset = Asset.objects.get(pk=a)
        s = asset.assigned()
        return {'asset': a, 'check_type': 'in', 'staff': s}

    def get_context_data(self, **kwargs):
        ctx = super(Checkin_Create, self).get_context_data(**kwargs)
        asset_id = self.kwargs['asset_id']
        ctx['asset'] = Asset.objects.get(id=asset_id)
        return ctx


class AssetTable(tables.Table):
    no = tables.Column(accessor='no')
    link = tables.LinkColumn(
        'asset_view',
        args=[A('pk')],
        orderable=False,
        text='View'
    )

    class Meta:
        model = Asset
        fields = ['no', 'descr', 'office', 'program']
        attrs = {'class': 'paleblue'}


@login_required
def asset_list(request):
    assets = Asset.objects.all()
    table = AssetTable(assets)
    f = AssetFilter(request.GET, queryset=Asset.objects.all())

    return render(
        request,
        'assets/asset_list.html',
        {'assets': assets, 'table': table, 'f': f}
    )


@permission_required('assets.can_download_assets')
def download_assets(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Asset Data"'
    writer = csv.writer(response)
    t = timezone.now()

    writer.writerow(['Asset Tracker Export', t, '', '', '', '', '', ''])

    writer.writerow([
        'Asset No',
        'Type',
        'Description',
        'Serial No',
        'Program',
        'Office',
        'Assigned To',
        'Assigned Staff ID'
    ])

    assets = Asset.objects.all()
    for asset in assets:
        writer.writerow([
            asset.no,
            asset.descr.name,
            asset.add_descr,
            asset.serial,
            asset.program.name,
            asset.office.name,
            asset.assigned(),
            asset.assigned().staff_id
        ])

    writer.writerow(['Asset Log Export', t, '', '', '', '', ])

    writer.writerow([
        'Asset No',
        'Asset Type',
        'Asset Description',
        'Staff',
        'Date',
        'In / Out',
    ])

    checks = Check.objects.all()
    for check in checks:
        writer.writerow([
            check.asset.no,
            check.asset.descr,
            check.asset.add_descr,
            check.staff,
            check.date,
            check.check_type
        ])

    return response
