from django.forms import ModelForm
from django import forms
from .models import Stores

class StoreForm(ModelForm):
    store_id = forms.IntegerField()
    store_name = forms.TextInput()
    phone = forms.TextInput()
    email = forms.TextInput()
    street = forms.TextInput()
    city = forms.TextInput()
    state = forms.TextInput()
    zip_code = forms.TextInput()

    class Meta:
        model = Stores
        fields = ['store_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code']