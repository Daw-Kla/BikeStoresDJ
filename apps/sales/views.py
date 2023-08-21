from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from .models import *
import json

#views take one argument 'request' 
def customers_table(request):
    context = {}
    return render(request, 'apps\templates\home\customers_table.html', context)

def customers(request):
    result_list = list(Customers.objects.all().values(\
        'first_name', 'last_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code'))
    return JsonResponse(result_list, safe=False)

def stores_table(request):
    context = {}
    return render(request, 'apps\templates\home\stores_table.html', context)

def stores(request):
    result_list = list(Stores.objects.all().values('store_id', 'store_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code'))
    return JsonResponse(result_list, safe=False)

def order_items_table(request):
    context = {}
    return render(request, 'apps\templates\home\order_items_table.html', context)

def order_items(request):
    result_list = list(OrderItems.objects.all().values('order', 'item_id', 'product', 'quantity', 'list_price', 'discount'))
    return JsonResponse(result_list, safe=False)

def orders_table(request):
    context = {}
    return render(request, 'apps\templates\home\orders_table.html', context)

def orders(request):
    result_list = list(Orders.objects.all().values('order_id', 'customer', 'order_status', 'order_date', 'store', 'staff'))
    return JsonResponse(result_list, safe=False)

def staffs_table(request):
    context = {}
    return render(request, 'apps\templates\home\staffs_table.html', context)

def staffs(request):
    result_list = list(Staffs.objects.all().values('staff_id', 'first_name', 'last_name', 'email', 'phone', 'active', 'store', 'manager'))
    return JsonResponse(result_list, safe=False)