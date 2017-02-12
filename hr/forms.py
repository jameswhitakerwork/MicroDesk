from django.forms import ModelForm
from .models import Staff, Contract, Position
from django import forms

"""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependText, PrependAppendedText, FormActions)
"""


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        exclude = ['', ]
        help_texts = {
            'user': 'If the staff member has created an account on this site, you can link it to their staff profile here.'
        }
        widgets = {
            'entry_on_duty': forms.SelectDateWidget
        }


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        exclude = ['', ]
        widgets = {
            'start_date': forms.SelectDateWidget,
            'end_date': forms.SelectDateWidget
        }


class PositionForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['', ]
        widgets = {
            'start_date': forms.SelectDateWidget,
            'expected_need_until': forms.SelectDateWidget
        }
