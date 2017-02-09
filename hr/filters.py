import django_filters
from .models import Staff


class StaffFilter(django_filters.FilterSet):

    class Meta:
        model = Staff
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }
