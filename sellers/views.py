from email import message
from django.shortcuts import render
from common.models import Seller

from sellers.models import Products

# Create your views here.

def seller_home(request):
    return render(request,'seller_home.html')

def add_product(request):

    message = ""
    if request.method == 'POST':
        name = request.POST["pname"]
        price= request.POST["pprice"]
        description = request.POST["pdescription"]
        availability = request.POST["pquantity"]
        image = request.FILES["pimg"]
        seller = Seller.objects.get(seller_id=request.session['seller'])

        new_product=Products(product_name=name,price=price,description=description,stock=availability,product_image=image,seller_id=seller)
        new_product.save()

        message="Sucessfully added the product"
    return render(request,'add_product.html',{'msg':message})

def view_product(request):

    seller_product = Products.objects.filter(seller_id=request.session['seller'])  

    seller = Seller.objects.get(seller_id =  request.session['seller']) 
    return render(request,'view_product.html',{'products':seller_product,'sellers':seller})

def view_order(request):
    return render(request,'view_orders.html')

def change_password(request):
    return render(request,'change_password.html')
