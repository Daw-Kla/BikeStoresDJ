from typing import Any, Dict
from django.forms import ModelForm
from django import forms
from .models import Stores, Staffs


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


ACTIVE_CHOICES = ((0, 'Inactive'),(1, 'Active'),)

class StaffForm(forms.Form):

    first_name = forms.CharField(
        label='First name:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'first_name',
                'class': 'form-control form-control-sm',
                'placeholder': 'First name'
            }
        )
    )
    last_name = forms.CharField(
        label='Last name:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'last_name',
                'class': 'form-control form-control-sm',
                'placeholder': 'Last name'
            }
        )
    )
    email = forms.CharField(
        label='Email:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'email',
                'class': 'form-control form-control-sm',
                'placeholder': 'Email'
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
    active = forms.ChoiceField(
        choices=ACTIVE_CHOICES,
        label='Active:',
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'active',
                'class': 'form-control form-control-sm',
                'placeholder': 'Is staff member acitve?'
            }
        )
    )
    store = forms.ModelChoiceField(
        queryset=Stores.objects.all(),
        label='Store:',
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'store',
                'placeholder': '-----',
                'class': 'form-control form-control-sm',
            }
        )
    )
    manager = forms.ModelChoiceField(
        queryset=Staffs.objects.all(),
        label='Manager:',
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'manager',
                'placeholder': '-----',
                'class': 'form-control form-control-sm',
            }
        )
    )
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        active = cleaned_data.get("active")
        store = cleaned_data.get("store")
        manager = cleaned_data.get("manager")

class CustomerForm(forms.Form):

    first_name = forms.CharField(
        label='First name:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'first_name',
                'class': 'form-control form-control-sm',
                'placeholder': 'First name'
            }
        )
    )
    last_name = forms.CharField(
        label='Last name:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'last_name',
                'class': 'form-control form-control-sm',
                'placeholder': 'Last name'
            }
        )
    )
    phone = forms.CharField(
        label='Phone:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'name': 'phone',
                'class': 'form-control form-control-sm',
                'placeholder': 'Phone'
            }
        )
    )
    email = forms.CharField(
        label='Email:',
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
        label='Zip_code:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'zip_code',
                'class': 'form-control form-control-sm',
                'placeholder': 'Zip_code'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")
        street = cleaned_data.get("street")
        city = cleaned_data.get("city")
        state = cleaned_data.get("state")
        zip_code = cleaned_data.get("zip_code")
