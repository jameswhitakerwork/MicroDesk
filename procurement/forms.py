from django.forms import ModelForm
from .models import PurchaseRequest, JSignatureModel, PurchaseItem, WBS, PRStatus
from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from django.forms.models import inlineformset_factory

"""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependText, PrependAppendedText, FormActions)
"""

years = [x for x in range(2000, 2025)]


class PRForm(ModelForm):
    class Meta:
        model = PurchaseRequest
        exclude = ['pr_no', ]
        widgets = {'pr_date_needed': forms.SelectDateWidget(years=years)}


class PRAjaxForm(ModelForm):
    class Meta:
        model = PurchaseRequest
        exclude = [
            'pr_creator',
            'pr_date_prepared',
            'status',
            'sig1',
            'sig2',
            'sig3',
            'sig4',
            'pr_no'
        ]
        labels = {
            'pr_requisitioner': 'Requisitioner',
            'pr_program': 'Program',
            'pr_department': 'Department',
            'pr_office': 'Office',
            'pr_date_needed': 'Date Required',
            'pr_justification': 'Justification'}
        widgets = {'pr_date_needed': forms.SelectDateWidget(years=years)}


class PRCreateForm(ModelForm):
    class Meta:
        model = PurchaseItem
        exclude = ['totalprice', 'pr']


PRCreateFormSet = inlineformset_factory(
    PurchaseRequest,
    PurchaseItem,
    form=PRCreateForm,
    extra=1,
    widgets={'pr_date_needed': forms.SelectDateWidget(years=years)}
)


class SignatureForm(forms.Form):
    signature = JSignatureField()
