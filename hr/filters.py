import django_filters
from django_filters import ChoiceFilter
from .models import *


class StaffFilter(django_filters.FilterSet):
    PROGRAM_CHOICES = (
        (1, 'TMRP'),
        (2, 'CADRE')
    )

    program = ChoiceFilter(
        name='program',
        method='filter_program',
        choices=PROGRAM_CHOICES
    )

    def filter_program(self, queryset, name, value):
        print 'passed queryset: '
        print queryset
        print 'passed choice value: '
        print value
        print 'test relationship lookup: '
        print queryset.filter(contract__position__program__id=2)
        print 'test value get: '
        print Position.objects.filter(program_id=2)
        print 'program lookup: '
        print queryset.filter(contract__position__program__id=2)
        return queryset.filter(contract__position__program__id=2)

    class Meta:
        model = Staff
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }
