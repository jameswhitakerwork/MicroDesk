import django_filters
from django_filters import ChoiceFilter, BooleanFilter
from .models import *

class AssetFilter(django_filters.FilterSet):
    os = Office.objects.all()
    OFFICE_CHOICES = ((o.id, o.name) for o in os)

    ps = Program.objects.all()
    PROGRAM_CHOICES = ((p.id, p.name) for p in ps)

    ts = AssetType.objects.all()
    ASSETTYPE_CHOICES = ((t.id, t.name) for t in ts)

    office_filter = ChoiceFilter(
        label='Office',
        method='filter_office',
        choices=OFFICE_CHOICES
    )

    program_filter = ChoiceFilter(
        label='Program',
        method='filter_program',
        choices=PROGRAM_CHOICES
    )

    assettype_filter = ChoiceFilter(
        label='Asset Type',
        method='filter_assettype',
        choices=ASSETTYPE_CHOICES
    )

    def filter_office(self, queryset, name, value):
        return queryset.filter(office__id=value)

    def filter_program(self, queryset, name, value):
        return queryset.filter(program__id=value)

    def filter_assettype(self, queryset, name, value):
        return queryset.filter(asset_type__id=value)

    class Meta:
        object = Asset
        exclude = ['', ]