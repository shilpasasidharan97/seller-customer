from itertools import product
from django.shortcuts import render

from common.models import Customer
from sellers.models import Products

# Create your views here.


def customer_home(request):

    customer = Customer.objects.get(cust_id =  request.session['customer'])

    products = Products.objects.all()
    

    return render(request, 'customer_home.html', {'customer': customer,'product':products })


def view_cart(request):
    return render(request, 'view_cart.html')


def view_order(request):
    return render(request, 'view_orders.html')
