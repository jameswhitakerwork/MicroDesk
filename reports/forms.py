from django.forms import ModelForm
from .models import Report
from django import forms

years = [x for x in range(2000, 2025)]


class ReportForm(ModelForm):
    class Meta:
        model = Report
        exclude = ['report', ]
        help_texts = {
        }
        widgets = {
            'deadline': forms.SelectDateWidget(years=years)
        }
        labels = {
            'reportee': 'Email address of reportee',
        }

class ReportSubmitForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report', ]
