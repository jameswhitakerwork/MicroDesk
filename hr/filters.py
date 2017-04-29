import django_filters
from django_filters import ChoiceFilter, BooleanFilter
from .models import *


class StaffFilter(django_filters.FilterSet):
    programs = Program.objects.all()
    ds = Duty_Station.objects.all()
    PROGRAM_CHOICES = ((p.id, p.name) for p in programs)
    DS_CHOICES = ((d.id, d.name) for d in ds)

    program_filter = ChoiceFilter(
        label='program',
        method='filter_program',
        choices=PROGRAM_CHOICES
    )

    duty_station_filter = ChoiceFilter(
        label='duty station',
        method='filter_duty_station',
        choices=DS_CHOICES
    )

    active_contract_filter = BooleanFilter(
        label='active contract',
        method='filter_active_contract'
    )

    def filter_program(self, queryset, name, value):
        return queryset.filter(contract__position__program__id=value)

    def filter_duty_station(self, queryset, name, value):
        print 'name: ' + name
        return queryset.filter(contract__position__duty_station__id=value)

    def filter_active_contract(self, queryset, name, value):
        value = 1 - value
        return queryset.filter(contract__isnull=value)

    class Meta:
        model = Staff
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }
