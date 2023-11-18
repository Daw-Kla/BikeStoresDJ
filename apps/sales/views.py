from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import StoreForm, StaffForm, CustomerForm, OrderForm, YearSelectForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
import json
import calendar
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.template import loader

from datetime import date
from apps.production.models import Brands, Categories
from django.db.models import Count

def customers_table(request):
    object_list = Customers.objects.all()
    data = []
    context = {}

    for item in object_list:
        data.append([item.customer_id, item.first_name, item.last_name, item.phone, item.email, item.street, item.city, item.state, item.zip_code])
    context['table'] = data

    if request.method =='POST':
        details = CustomerForm(request.POST)

        if details.is_valid():  
            cd = details.cleaned_data
            pc = Customers(first_name=cd['first_name'],
                        last_name=cd['last_name'],
                        phone=cd['phone'],
                        email=cd['email'],
                        street=cd['street'],
                        city=cd['city'],
                        state=cd['state'],
                        zip_code=cd['zip_code'],)
            pc.save() 
            pc = CustomerForm()
            return redirect('/customers_table/')
        else:
            return redirect('/customers_table/')
    else:
        pc = CustomerForm()

    context['table'] = data
    context['form'] = pc

    return render(request, 'sales\customers_table.html', context)

def edit_customer(request, customer_id):
    customer = Customers.objects.get(pk=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            customer.first_name = cd['first_name']
            customer.last_name = cd['last_name']
            customer.phone = cd['phone']
            customer.email = cd['email']
            customer.street = cd['street']
            customer.city = cd['city']
            customer.state = cd['state']
            customer.zip_code = cd['zip_code']
            customer.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CustomerForm(initial={
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'phone': customer.phone,
            'email': customer.email,
            'street': customer.street,
            'city': customer.city,
            'state': customer.state,
            'zip_code': customer.zip_code,})
        
    data = {
        'customer_id': customer_id,
        'form_data': {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'phone': customer.phone,
            'email': customer.email,
            'street': customer.street,
            'city': customer.city,
            'state': customer.state,
            'zip_code': customer.zip_code,
        }
    }

    return JsonResponse(data)

def get_customers_data(request):
    customers = Customers.objects.all()
    data = [[customer.customer_id, customer.first_name, customer.last_name, customer.phone, customer.email, customer.street, customer.city, customer.state, customer.zip_code] for customer in customers]
    return JsonResponse(data, safe=False)

def delete_customer(request, customer_id):
    if request.method == 'POST':
        store = Customers.objects.get(pk=customer_id)
        store.delete()
        return redirect('/customers_table/')
    
    return redirect('/stores_table/')

def edit_store(request, store_id):
    store = Stores.objects.get(pk=store_id)
    
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
    data = []
    context = {}
    for item in object_list:
        storeName = item.store.store_name if item.store else None
        y = item.staff.first_name if item.staff else None
        z = item.staff.last_name if item.staff else None
        staff = f'{y} {z}'
        data.append([item.order_id, item.customer, item.order_status, item.order_date, item.required_date, item.shipped_date, storeName, staff])

    if request.method =='POST': 
        details = OrderForm(request.POST)
        if details.is_valid(): 
            cd = details.cleaned_data
            store_instance = Stores.objects.get(store_name=cd['store'])
            staff_instance = Staffs.objects.get(pk=cd['staff'].pk)
            pc = Orders(customer=cd['customer'],
                        order_status=cd['order_status'],
                        order_date=cd['order_date'],
                        shipped_date=cd['shipped_date'],
                        required_date=cd['required_date'],
                        store=store_instance,
                        staff=staff_instance)
            pc.save() 
            pc = OrderForm()
            return redirect('/orders_table/')
        else:
            return redirect('/orders_table/')
    else:
        pc = OrderForm()

    context['table'] = data
    context['form'] = pc

    return render(request, 'sales\orders_table.html', context)

def edit_order(request, order_id):
    order = Orders.objects.get(pk=order_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order.customer = cd['customer']
            order.order_status = cd['order_status']
            order.order_date = cd['order_date']
            order.shipped_date = cd['shipped_date']
            order.required_date = cd['required_date']
            order.store = cd['store']
            order.staff = cd['staff']
            order.save()  # Zapisujemy zmienione dane do bazy danych
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = OrderForm(initial={
            'customer': order.customer if order.customer else None,
            'order_status': order.order_status,
            'order_date': order.order_date,
            'shipped_date': order.shipped_date,
            'required_date': order.required_date,
            'store': order.store_id if order.store else None,
            'staff': order.staff_id if order.staff else None,
        })

    data = {
        'order_id': order_id,
        'form_data': {
            'customer': f'{order.customer.first_name} {order.customer.last_name}' if order.customer else None,
            'order_status': order.order_status,
            'order_date': order.order_date,
            'shipped_date': order.shipped_date,
            'required_date': order.required_date,
            'store': order.store.store_name if order.store else None,
            'staff': f'{order.staff.first_name} {order.staff.last_name}' if order.staff else None,
        }
    }
    return JsonResponse(data, encoder=DjangoJSONEncoder)

def delete_order(request, order_id):
    if request.method == 'POST':
        order = Orders.objects.get(pk=order_id)
        order.delete()
        return redirect('/orders_table/')
    
    return redirect('/orders_table/')

def staffs_table(request):
    object_list = Staffs.objects.all()
    data = []
    context = {}
    #stores = Stores.objects.all()
    #print(x[1]['store__store_name'])
    for item in object_list:
        storeName = item.store.store_name if item.store else None
        y = item.manager.first_name if item.manager else None
        z = item.manager.last_name if item.manager else None
        manager = f'{y} {z}'
        data.append([item.staff_id, item.first_name, item.last_name, item.email, item.phone, item.active, storeName, manager])
    
    if request.method =='POST': 
        # Pass the form data to the form class
        details = StaffForm(request.POST)
        
        # In the 'form' class the clean function is defined, if all the data is correct as per the clean function, it returns true
        if details.is_valid(): 
            # Temporarily make an object to be add some logic into the data if there is such a need before writing to the database  
            cd = details.cleaned_data
            store_instance = Stores.objects.get(store_name=cd['store'])
            try:
                # check if there is a emlploeyy witch given no
                manager_instance = Staffs.objects.get(pk=cd['manager'].pk)
            except ObjectDoesNotExist:
                # if not then chacge instance
                manager_instance = None

            pc = Staffs(first_name=cd['first_name'],
                        last_name=cd['last_name'],
                        email=cd['email'],
                        phone=cd['phone'],
                        active=cd['active'],
                        store=store_instance,
                        manager=manager_instance,)
            pc.save() 
            pc = StaffForm()
            # after succesfull POST there is redirect to the same page for getinf out of POST method dooing GET 
            #(prevent from continous data send do DB after refreshing the page)
            return redirect('/staffs_table/')
        else:
            # Redirect back to the same page if the data was invalid
            return redirect('/staffs_table/')
    else:
        pc = StaffForm()

    context['table'] = data
    context['form'] = pc
    return render(request, 'sales\staffs_table.html', context)

def edit_staff(request, staff_id):
    staff = Staffs.objects.get(pk=staff_id)

    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            staff.first_name = cd['first_name']
            staff.last_name = cd['last_name']
            staff.email = cd['email']
            staff.phone = cd['phone']
            staff.active = cd['active']
            staff.store = cd['store']
            staff.manager = cd['manager']
            staff.save()  # Zapisujemy zmienione dane do bazy danych
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = StaffForm(initial={
            'first_name': staff.first_name,
            'last_name': staff.last_name,
            'email': staff.email,
            'phone': staff.phone,
            'active': staff.active,
            'store': staff.store_id if staff.store else None,
            'manager': staff.manager_id if staff.manager else None,
        })

        data = {
            'staff_id': staff_id,
            'form_data': {
                'first_name': staff.first_name,
                'last_name': staff.last_name,
                'email': staff.email,
                'phone': staff.phone,
                'active': staff.active,
                'store': staff.store,
                'manager': f'{staff.manager.first_name} {staff.manager.last_name}' if staff.manager else None,
            }
        }

        # Serializuj obiekt Stores do formatu JSON
        data['form_data']['store'] = staff.store.store_name if staff.store else None

        return JsonResponse(data, encoder=DjangoJSONEncoder)

def get_staffs_data(request):
    staffs = Staffs.objects.all()
    data = [{'staff_id': staff.staff_id,
             'first_name': staff.first_name,
             'last_name': staff.last_name,
             'email': staff.email,
             'phone': staff.phone,
             'active': staff.active,
             'store': staff.store.store_name if staff.store else None,
             'manager': f'{staff.manager.first_name} {staff.manager.last_name}' if staff.manager else None} for staff in staffs]
    #data do jsonresponse must be a list of lists
    data_list = [[staff['staff_id'], staff['first_name'], staff['last_name'], staff['email'], staff['phone'], staff['active'], staff['store'], staff['manager']] for staff in data]
    return JsonResponse(data_list, safe=False)

def delete_staff(request, staff_id):
    if request.method == 'POST':
        store = Staffs.objects.get(pk=staff_id)
        store.delete()
        return redirect('/staffs_table/')
    
    return redirect('/staffs_table/')

def charts_test(request):
    
    object_list = Orders.objects.all()
    data = []
    item_per_year ={}
    selected_year = None
    labels = []
    values = []
    
    if request.method == 'GET':
        selected_year = request.GET.get('years')

    years = set(item.order_date.year for item in object_list)  
    form = YearSelectForm(request.GET or None, initial={'years': selected_year})
    form.fields['years'].choices = [(year, year) for year in years]

    for item in object_list:
        data.append([item.order_id, item.customer, item.order_status, item.order_date, item.required_date, item.shipped_date, item.store, item.staff])

        if item.order_date.year not in item_per_year:
            item_per_year[item.order_date.year] = {}

        if item.order_date.month not in item_per_year[item.order_date.year]:
            item_per_year[item.order_date.year][item.order_date.month] = 1
        else:
            item_per_year[item.order_date.year][item.order_date.month] += 1

    for key, val in item_per_year[int(selected_year)].items():
        labels.append(calendar.month_name[key])
        values.append(val)

    brand_sales = Brands.objects.annotate(total_sales=Count('products__orderitems', filter=models.Q(products__orderitems__order__order_date__year=selected_year))).values('brand_name', 'total_sales')
    category_sales = Categories.objects.annotate(total_sales=Count('products__orderitems', filter=models.Q(products__orderitems__order__order_date__year=selected_year))).values('category_name', 'total_sales')

    brands = [entry['brand_name'] for entry in brand_sales]
    total_brands_sales = [entry['total_sales'] for entry in brand_sales]
    categories = [entry['category_name'] for entry in category_sales]
    total_categories_sales = [entry['total_sales'] for entry in category_sales]

    labeled_data = {'labels':labels, 'values':values, 'brands': brands, 'total_brands_sales': total_brands_sales, 
                    'categories': categories, 'total_categories_sales': total_categories_sales}
    json_data = json.dumps(labeled_data)

    return render(request, 'home/charts_test.html', {'form': form, 'json_data': json_data})