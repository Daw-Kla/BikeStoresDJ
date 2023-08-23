from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from .models import *
from .forms import StoreForm
from django.contrib import messages
import json

#views take one argument 'request' 
def customers_table(request):
    context = {}
    return render(request, 'apps\templates\home\customers_table.html', context)

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
    print(request.method)
    print('ok')

    if request.method == 'POST':
        context = {}
        form = StoreForm(request.POST or None)
        context['StoreForm'] = StoreForm

        if form.is_valid():
            print('sxsaxa')
            obj = Stores()

            obj.store_name = StoreForm.cleaned_data.get("store_name")
            obj.phone = StoreForm.cleaned_data.get("phone")
            obj.email = StoreForm.cleaned_data.get("email")
            obj.street = StoreForm.cleaned_data.get("street")
            obj.city = StoreForm.cleaned_data.get("city")
            obj.state = StoreForm.cleaned_data.get("state")
            obj.zip_code = StoreForm.cleaned_data.get("zip_code")
            

            try:
                messages.success(request, "Adding Store done")
                obj.save()
                return(request)
            except:
                messages.error(request, "Adding Store not done")
                context['error'] = "Adding aborted"
        else:
            print(form.errors)
     
    return render(request, 'apps\templates\home\stores_table.html', context)


'''#testowe nie działające wyświetlanie formsa
def test(request):
    form = StoreForm(request.POST)
    context = {'form' : form}
    return render(request, 'test.html', context)'''


def stores(request):
    result_list = list(Stores.objects.all().values('store_id', 'store_name', 'phone', 'email', 'street', 'city', 'state', 'zip_code'))
    return JsonResponse(result_list, safe=False)

def order_items_table(request):
    context = {}
    return render(request, 'apps\templates\home\order_items_table.html', context)

#using product__product_name allows to get full product name in jsonresponse and not only related product objcet number
def order_items(request):
    result_list = list(OrderItems.objects.all().values('order', 'item_id', 'product__product_name', 'quantity', 'list_price', 'discount'))
    return JsonResponse(result_list, safe=False)

def orders_table(request):
    context = {}
    return render(request, 'apps\templates\home\orders_table.html', context)

def orders(request):
    result_list = list(Orders.objects.all().values('order_id', 'customer', 'order_status', 'order_date', 'store__store_name', 'staff__first_name', 'staff__last_name'))
    return JsonResponse(result_list, safe=False)

def staffs_table(request):
    context = {}
    return render(request, 'apps\templates\home\staffs_table.html', context)

def staffs(request):
    result_list = list(Staffs.objects.all().values('staff_id', 'first_name', 'last_name', 'email', 'phone', 'active', 'store__store_name', 'manager__first_name', 'manager__last_name'))
    return JsonResponse(result_list, safe=False)