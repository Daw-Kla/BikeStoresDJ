from typing import Any, Dict
from django.forms import ModelForm
from django import forms
from .models import Stores

class StoreForm(forms.Form):

    store_name = forms.CharField(
        label='store_name: *',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'Store name',
                'class': 'form-control form-control-sm',
                'placeholder': 'store_name'
            }
        )
    )

    phone = forms.CharField(
        label='phone: *',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'phone',
                'class': 'form-control form-control-sm',
                'placeholder': 'Phone'
            }
        )
    )

    email = forms.CharField(
        label='email: *',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'email',
                'class': 'form-control form-control-sm',
                'placeholder': 'Email'
            }
        )
    )

    street = forms.CharField(
        label='street: *',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'street',
                'class': 'form-control form-control-sm',
                'placeholder': 'Street'
            }
        )
    )

    city = forms.CharField(
        label='city: *',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'city',
                'class': 'form-control form-control-sm',
                'placeholder': 'City'
            }
        )
    )

    state = forms.CharField(
        label='state: *',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'state',
                'class': 'form-control form-control-sm',
                'placeholder': 'State'
            }
        )
    )

    zip_code = forms.CharField(
        label='zip_code: *',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'zip_code',
                'class': 'form-control form-control-sm',
                'placeholder': 'Zip code'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        store_name = cleaned_data.get("store_name")
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")
        street = cleaned_data.get("street")
        city = cleaned_data.get("city")
        state = cleaned_data.get("state")
        zip_code = cleaned_data.get("zip_code")