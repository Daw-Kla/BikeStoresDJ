from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from .models import *
from .forms import StoreForm, MyForm
from django.contrib import messages
import json
from django.template import loader

#views take one argument 'request' 


def customers_table(request):
    object_list = Customers.objects.all()
    dane = []
    context = {}
    for item in object_list:
        dane.append([item.first_name, item.last_name, item.phone, item.email, item.street, item.city, item.state, item.zip_code])
    context['tabela'] = dane
    return render(request, 'sales\customers_table.html', context)

def customers(request):
    result_list = list(Customers.objects.all().values(\
        'first_name', 'last_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code'))
    return JsonResponse(result_list, safe=False)

'''
def stores_table(request):

    if request.method == 'POST':
        print('przed post')
        store_id = request.POST['store_id']
        store_name = request.POST['store_name']
        phone = request.POST['phone']
        email = request.POST['email']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        print('pp post')
        new_store = Stores(store_id=store_id, store_name=store_name, phone=phone, email=email, street=street, city=city, state=state, zip_code=zip_code)
        new_store.save()
        print('po save')

    context = {}
    return render(request, 'apps\templates\home\stores_table.html', context)'''

#@ensure_csrf_cookie


def stores_table(request):
    object_list = Stores.objects.all()
    dane = []
    context = {}
    for item in object_list:
        dane.append([item.store_id, item.store_name, item.phone, item.email, item.street, item.city, item.state, item.zip_code])
    context['tabela'] = dane
    return render(request, 'sales\stores_table.html', context)

def stores(request):
    result_list = list(Stores.objects.all().values('store_id', 'store_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code'))
    return JsonResponse(result_list, safe=False)


#testowe nie działające wyświetlanie formsa
# Create your views here.
'''def form_handle(request):
    if request.method == 'POST':
        form = MyForm(request.POST) # if post method then form will be validated
        if form.is_valid():
            cd = form.cleaned_data
            num1 = cd.get('num1')
            num2 = cd.get('num2')
            result = cd.get('result')
            if float(num1) + float(num2) == float(result):
                # give HttpResponse only or render page you need to load on success
                return HttpResponse("valid entiries")
            else:
                # if sum not equal... then redirect to custom url/page 
                return HttpResponseRedirect('/')  # mention redirect url in argument

    else:
        form = MyForm() # blank form object just to pass context if not post method
    return render(request, "test.html", {'form': form})'''


#szybsze wczytywanie
'''def load_page_order_items(request, page):
    items_per_page = 50
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    object_list = OrderItems.objects.all()
    dane = []

    for item in object_list[start_index:end_index]:
        productName = item.product.product_name if item.product else None
        dane.append([item.order, item.item_id, productName, item.quantity, item.list_price, item.discount])

    return JsonResponse(dane, safe=False)

def order_items_table(request):
    context = {}
    return render(request, 'sales\order_items_table.html', context)'''

def order_items_table(request):
    object_list = OrderItems.objects.all()
    dane = []
    context = {}
    for item in object_list:
        productName = item.product.product_name if item.product else None
        dane.append([item.order, item.item_id, productName, item.quantity, item.list_price, item.discount,])
    context['tabela'] = dane
    return render(request, 'sales\order_items_table.html', context)

#using product__product_name allows to get full product name in jsonresponse and not only related product objcet number
def order_items(request):
    result_list = list(OrderItems.objects.all().values('order', 'item_id', 'product__product_name', 'quantity', 'list_price', 'discount'))
    return JsonResponse(result_list, safe=False)

def orders_table(request):
    object_list = Orders.objects.all()
    dane = []
    context = {}
    for item in object_list:
        storeName = item.store.store_name if item.store else None
        y = item.staff.first_name if item.staff else None
        z = item.staff.last_name if item.staff else None
        staff = f'{y} {z}'
        dane.append([item.order_id, item.customer, item.order_status, item.order_date, storeName, staff])
    context['tabela'] = dane
    return render(request, 'sales\orders_table.html', context)

def orders(request):
    result_list = list(Orders.objects.all().values('order_id', 'customer', 'order_status', 'order_date', 'store__store_name', 'staff__first_name', 'staff__last_name'))
    return JsonResponse(result_list, safe=False)

def staffs_table(request):
    object_list = Staffs.objects.all()
    dane = []
    context = {}
    #print(x[1]['store__store_name'])
    for item in object_list:
        storeName = item.store.store_name if item.store else None
        y = item.manager.first_name if item.manager else None
        z = item.manager.last_name if item.manager else None
        manager = f'{y} {z}'
        dane.append([item.staff_id, item.first_name, item.last_name, item.email, item.phone, item.active, storeName, manager])
    
    context['tabela'] = dane
    return render(request, 'sales\staffs_table.html', context)

def staffs(request):
    result_list = list(Staffs.objects.all().values('staff_id', 'first_name', 'last_name', 'email', 'phone', 'active', 'store__store_name', 'manager__first_name', 'manager__last_name'))
    return JsonResponse(result_list, safe=False)