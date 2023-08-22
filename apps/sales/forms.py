from django import forms
from .models import Stores

class StoreForm(forms.ModelForm):
    class Meta:
        model = Stores
        fields = ['store_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code']