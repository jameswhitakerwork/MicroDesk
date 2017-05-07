import django_filters
from django_filters import ChoiceFilter, BooleanFilter
from .models import Report
from hr.models import Program


class ReportFilter(django_filters.FilterSet):
    submitted_filter = BooleanFilter(
        label = 'Submitted?,',
        method='filter_submitted'
    )

    def filter_submitted(self, queryset, name, value):
        value = 1 - value
        return queryset.filter(report__isnull=value)

    class Meta:
        model = Report
        exclude = [
            'report',
            'deadline',
            'reportee',
            'name',
        ]
