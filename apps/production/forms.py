from typing import Any, Dict
from django.forms import ModelForm
from django import forms
from .models import Stocks, Products, Brands, Categories
from apps.sales.models import Stores

class StockForm(forms.Form):
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

    product = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        label='Product:',
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'product',
                'placeholder': '-----',
                'class': 'form-control form-control-sm',
            }
        )
    )

    quantity = forms.IntegerField(
        label='Quantity',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'quantity',
                'class': 'form-control form-control-sm',
                'placeholder': 'Quantity'
            }
        )
    )

    def clean(self):
            cleaned_data = super().clean()
            store = cleaned_data.get("store")
            product = cleaned_data.get("product")
            quantity = cleaned_data.get("quantity")


class ProductForm(forms.Form):
    product_name = forms.CharField(
        label='Product name:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'product_name',
                'class': 'form-control form-control-sm',
                'placeholder': 'Product name'
            }
        )
    )

    brand = forms.ModelChoiceField(
        queryset=Brands.objects.all(),
        label='Brand:',
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'brand',
                'placeholder': '-----',
                'class': 'form-control form-control-sm',
            }
        )
    )

    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        label='Category:',
        required=True,
        widget=forms.Select(
            attrs={
                'name': 'category',
                'placeholder': '-----',
                'class': 'form-control form-control-sm',
            }
        )
    )

    model_year = forms.IntegerField(
        label='Model year:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'model_year',
                'class': 'form-control form-control-sm',
                'placeholder': 'Model year'
            }
        )
    )

    list_price = forms.DecimalField(
        label='List price:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'list_price',
                'class': 'form-control form-control-sm',
                'placeholder': 'List price'
            }
        )
    )

    def clean(self):
            cleaned_data = super().clean()
            product_name = cleaned_data.get("product_name")
            brand = cleaned_data.get("brand")
            category = cleaned_data.get("category")
            model_year = cleaned_data.get("model_year")
            list_price = cleaned_data.get("list_price")