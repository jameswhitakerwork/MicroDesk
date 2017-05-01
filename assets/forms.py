from django.forms import ModelForm
from django.contrib.admin.widgets import AdminFileWidget
from .models import Asset, Check
from django import forms

years = [x for x in range(2000, 2025)]


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        exclude = ['', ]
        widgets = {'capitalized': forms.SelectDateWidget(years=years)}
        labels = {
            'descr': 'Description',
            'add_descr': 'Additional Description',
        }


class Checkin_Form(ModelForm):
    class Meta:
        model = Check
        exclude = ['',]
        labels = {
            'document': 'Asset Return Form (signed)',
        }
        widgets = {
            'asset': forms.HiddenInput(),
            'staff': forms.HiddenInput(),
            'check_type': forms.HiddenInput(),
            'document': AdminFileWidget,
        }


class Checkout_Form(ModelForm):
    class Meta:
        model = Check
        exclude = ['',]
        labels = {
            'document': 'Asset Assignment Form (signed)',
        }
        widgets = {
            'asset': forms.HiddenInput(),
            'check_type': forms.HiddenInput(),
            'document': AdminFileWidget,
        }
