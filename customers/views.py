from itertools import product
from django.http import HttpResponse
from django.shortcuts import redirect, render

from common.models import Customer, Seller
from customers.models import Cart, Order
from decorators import auth_customer
from sellers.models import Products

from django.conf import settings
from django.core.mail import send_mail

import socket
socket.getaddrinfo('localhost', 8080)

# Create your views here.

@auth_customer
def customer_home(request):

    

    customers = Customer.objects.get(cust_id =  request.session['customer'])

    products = Products.objects.all()
    

    return render(request, 'customer_home.html', {'customer': customers,'product':products })

@auth_customer
def view_cart(request):

    cart_products=Cart.objects.filter(customer_id=request.session['customer'])

    return render(request, 'view_cart.html',{'cartproduct':cart_products,})

@auth_customer
def view_order(request):
    orders=Order.objects.filter(customer_id=request.session['customer'])
    
    return render(request, 'view_orders.html',{'orders':orders,})
    
@auth_customer
def change_password(request):
    msg=""
    if request.method=='POST':
        old_psw=request.POST['oldpsw']
        new_psw=request.POST['newpsw']
        c_psw=request.POST['cpsw']
        customer_data=Customer.objects.get(cust_id=request.session['customer'])

        if customer_data.cust_password==old_psw:
            if new_psw==c_psw:
                Customer.objects.filter(cust_id=request.session['customer']).update(cust_password=new_psw)
                msg="successfully reset the password"
            else:
                msg="Mismatch"
        else:
            msg="Incorrect password.."
    return render(request,'change_password.html',{'msg':msg,})

@auth_customer
def add_to_cart(request,id):
    product_id=Products.objects.get(p_id=id)
    customer_id=Customer.objects.get(cust_id=request.session['customer'])

    cart_exist=Cart.objects.filter(customer_id=request.session['customer'],product_id=product_id).exists()

    if not cart_exist:
        new_cart=Cart(product_id=product_id,customer_id=customer_id)
        new_cart.save()

    return redirect('customers:custhome')


def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:customlogin')


def order(request,pid):
    msg=""
    product=Products.objects.get(p_id=pid)

    if request.method=='POST':
        
        customer_id=Customer.objects.get(cust_id=request.session['customer'])
        seller_id=Seller.objects.get(seller_id=product.seller_id.seller_id)
        quantity=request.POST['quantity']
        ship_address=request.POST['address']
        total_price=int(quantity)*product.price

        order=Order(product_id=product,customer_id=customer_id,seller_id=seller_id,quantity=quantity,shipping_address=ship_address,total_amount=total_price)
        order.save()

        send_mail("Order details","your order for ----- is placed successfully",settings.EMAIL_HOST_USER,[str(customer_id.cust_email)])
        product.stock=product.stock-int(quantity)
        product.save()
        msg="ordered"
        return redirect('customers:custhome')
        
        
    return render(request,'order.html',{'msg':msg,'product':product})



