from typing import Any, Dict
from django.forms import ModelForm
from django import forms
from .models import Stores


class StoreForm(forms.Form):

    store_name = forms.CharField(
        label='Store name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'store_name',
                'class': 'form-control form-control-sm',
                'placeholder': 'Store name',
                'id': 'store_id'
            }
        )
    )

    phone = forms.CharField(
        label='Phone:',
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
        label='E-mail:',
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
        label='Street:',
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
        label='City:',
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
        label='State:',
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
        label='Zip code:',
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
