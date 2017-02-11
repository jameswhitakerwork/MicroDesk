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


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        exclude = ['', ]


class PositionForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['', ]
