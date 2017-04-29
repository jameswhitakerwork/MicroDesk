from django.forms import ModelForm
from .models import Staff, Contract, Position, JSignatureModel
from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

"""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependText, PrependAppendedText, FormActions)
"""

years = [x for x in range(2000, 2025)]


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        exclude = ['', ]
        help_texts = {
            'user': 'If the staff member has created an account on this site, you can link it to their staff profile here.'
        }
        widgets = {
            'entry_on_duty': forms.SelectDateWidget(years=years)
        }


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        exclude = ['', ]
        widgets = {
            'start_date': forms.SelectDateWidget(years=years),
            'end_date': forms.SelectDateWidget(years=years)
        }


class PositionForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['', ]
        widgets = {
            'start_date': forms.SelectDateWidget(years=years),
            'expected_need_until': forms.SelectDateWidget(years=years)
        }


class SignatureForm(forms.Form):
    signature = JSignatureField()
