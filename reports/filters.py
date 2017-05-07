import django_filters
from django_filters import ChoiceFilter, BooleanFilter
from .models import Report
from hr.models import Program


class ReportFilter(django_filters.FilterSet):

    class Meta:
        model = Report
        exclude = [
            'report',
            'deadline',
        ]
