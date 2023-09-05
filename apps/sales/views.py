from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from .models import *
from .forms import StoreForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
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

'''def customers(request):
    result_list = list(Customers.objects.all().values(\
        'first_name', 'last_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code'))
    return JsonResponse(result_list, safe=False)'''

def edit_store(request, store_id):
    store = Stores.objects.get(pk=store_id)
    print('in editr')
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            store.store_name = cd['store_name']
            store.phone = cd['phone']
            store.email = cd['email']
            store.street = cd['street']
            store.city = cd['city']
            store.state = cd['state']
            store.zip_code = cd['zip_code']
            store.save()  # Zapisujemy zmienione dane do bazy danych
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = StoreForm(initial={
            'store_name': store.store_name,
            'phone': store.phone,
            'email': store.email,
            'street': store.street,
            'city': store.city,
            'state': store.state,
            'zip_code': store.zip_code,
        })

    data = {
        'store_id': store_id,
        'form_data': {
            'store_name': store.store_name,
            'phone': store.phone,
            'email': store.email,
            'street': store.street,
            'city': store.city,
            'state': store.state,
            'zip_code': store.zip_code,
        }
    }
    return JsonResponse(data)

def delete_store(request, store_id):
    if request.method == 'POST':
        store = Stores.objects.get(pk=store_id)
        store.delete()
        return redirect('/stores_table/')
    
    return redirect('/stores_table/')

def get_stores_data(request):
    stores = Stores.objects.all()
    data = [[store.store_id, store.store_name, store.phone, store.email, store.street, store.city, store.state, store.zip_code] for store in stores]
    return JsonResponse(data, safe=False)

def stores_table(request):
    object_list = Stores.objects.all()
    data = []
    context = {}

    for item in object_list:
        data.append([item.store_id, item.store_name, item.phone, item.email, item.street, item.city, item.state, item.zip_code])
    
    if request.method =='POST': 
        # Pass the form data to the form class
        details = StoreForm(request.POST)
        # In the 'form' class the clean function is defined, if all the data is correct as per the clean function, it returns true
        if details.is_valid(): 
            # Temporarily make an object to be add some logic into the data if there is such a need before writing to the database  
            cd = details.cleaned_data
            pc = Stores(store_name=cd['store_name'],
                        phone=cd['phone'],
                        email=cd['email'],
                        street=cd['street'],
                        city=cd['city'],
                        state=cd['state'],
                        zip_code=cd['zip_code'])
            pc.save() 
            pc = StoreForm()
            # after succesfull POST there is redirect to the same page for getinf out of POST method dooing GET 
            #(prevent from continous data send do DB after refreshing the page)
            return redirect('/stores_table/')
        else:
            # Redirect back to the same page if the data was invalid
            return redirect('/stores_table/')
    else:
        pc = StoreForm()

    context['table'] = data
    context['form'] = pc
    
    return render(request, 'sales\stores_table.html', context)

'''def stores(request):
    result_list = list(Stores.objects.all().values('store_id', 'store_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code'))
    return JsonResponse(result_list, safe=False)'''


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
'''def order_items(request):
    result_list = list(OrderItems.objects.all().values('order', 'item_id', 'product__product_name', 'quantity', 'list_price', 'discount'))
    return JsonResponse(result_list, safe=False)'''

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

'''def orders(request):
    result_list = list(Orders.objects.all().values('order_id', 'customer', 'order_status', 'order_date', 'store__store_name', 'staff__first_name', 'staff__last_name'))
    return JsonResponse(result_list, safe=False)'''

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

'''def staffs(request):
    result_list = list(Staffs.objects.all().values('staff_id', 'first_name', 'last_name', 'email', 'phone', 'active', 'store__store_name', 'manager__first_name', 'manager__last_name'))
    return JsonResponse(result_list, safe=False)'''

