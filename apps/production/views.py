# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import StockForm, ProductForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def stocks_table(request):
    object_list = Stocks.objects.all()
    data = []
    context = {}

    for item in object_list:
        data.append([item.id, item.store, item.product, item.quantity])
    
    if request.method =='POST': 
        details = StockForm(request.POST)
        if details.is_valid(): 
            cd = details.cleaned_data
            pc = Stocks(store=cd['store'],
                        product=cd['product'],
                        quantity=cd['quantity'])
            pc.save() 
            pc = StockForm()
            return redirect('/stocks_table/')
        else:
            return redirect('/stocks_table/')
    else:
        pc = StockForm()

    context['table'] = data
    context['form'] = pc
    
    return render(request, 'production\stocks_table.html', context)

def edit_stock(request, id):
    stock = Stocks.objects.get(pk=id)
    
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            stock.store = cd['store']
            stock.product = cd['product']
            stock.quantity = cd['quantity']
            stock.save()  # Zapisujemy zmienione dane do bazy danych
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = StockForm(initial={
            'store': stock.store_id if stock.store else None,
            'product': stock.product,
            'quantity': stock.quantity,
        })

    data = {
        'id': id,
        'form_data': {
            'store': stock.store.store_name if stock.store else None,
            'product': stock.product.product_name if stock.product else None,
            'quantity': stock.quantity,
        }
    }
    return JsonResponse(data, encoder=DjangoJSONEncoder)

def delete_stock(request, id):
    if request.method == 'POST':
        store = Stocks.objects.get(pk=id)
        store.delete()
        return redirect('/stocks_table/')
    
    return redirect('/stocks_table/')

def products_table(request):
    object_list = Products.objects.all()
    data = []
    context = {}

    for item in object_list:
        data.append([item.product_id, item.product_name, item.brand, item.category, item.model_year, item.list_price])
    
    if request.method =='POST': 
        details = ProductForm(request.POST)
        if details.is_valid(): 
            cd = details.cleaned_data
            pc = Products(product_name=cd['product_name'],
                        brand=cd['brand'],
                        category=cd['category'],
                        model_year=cd['model_year'],
                        list_price=cd['list_price'])
            pc.save() 
            pc = ProductForm()
            return redirect('/products_table/')
        else:
            return redirect('/products_table/')
    else:
        pc = ProductForm()

    context['table'] = data
    context['form'] = pc
    
    return render(request, 'production\products_table.html', context)

def edit_product(request, product_id):
    product = Products.objects.get(pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product.product_name = cd['product_name']
            product.brand = cd['brand']
            product.category = cd['category']
            product.model_year = cd['model_year']
            product.list_price = cd['list_price']
            product.save()  # Zapisujemy zmienione dane do bazy danych
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductForm(initial={
            'product_name': product.product_name,
            'brand': product.brand_id if product.brand else None,
            'category': product.category_id if product.category else None,
            'model_year': product.model_year,
            'list_price': product.list_price,
        })

    data = {
        'product_id': product_id,
        'form_data': {
            'product_name': product.product_name,
            'brand': product.brand.brand_name if product.brand else None,
            'category': product.category.category_name if product.category else None,
            'model_year': product.model_year,
            'list_price': product.list_price,
        }
    }
    return JsonResponse(data, encoder=DjangoJSONEncoder)

def delete_product(request, product_id):
    print('in widok delete')
    if request.method == 'POST':
        print('in post ')
        product = Products.objects.get(pk=product_id)
        product.delete()
        return redirect('/products_table/')
    
    return redirect('/products_table/')