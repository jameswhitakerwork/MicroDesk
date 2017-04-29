import django_filters
from django_filters import ChoiceFilter, BooleanFilter
from .models import *


class PRFilter(django_filters.FilterSet):
    os = Office.objects.all()
    OFFICE_CHOICES = ((o.id, o.name) for o in os)

    ss = PRStatus.objects.all()
    PRSTATUS_CHOICES = ((s.id, s.status) for s in ss)

    office_filter = ChoiceFilter(
        label='office',
        method='filter_office',
        choices=OFFICE_CHOICES
    )

    status_filter = ChoiceFilter(
        label='status',
        method='filter_status',
        choices=PRSTATUS_CHOICES
    )

    def filter_office(self, queryset, name, value):
        return queryset.filter(office__id=value)

    class Meta:
        model = PurchaseRequest
        exclude = [
            'sig1',
            'sig2',
            'sig3',
            'sig4',
            'pr_date_needed',
            'pr_date_prepared',
            'pr_justification',
            'status'
        ]
