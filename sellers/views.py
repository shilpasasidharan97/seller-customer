from email import message
from django.shortcuts import redirect, render
from common.models import Seller
from customers.models import Cart, Order

from sellers.models import Products

# Create your views here.

def seller_home(request):
    seller = Seller.objects.get(seller_id =  request.session['seller']) #for displaying the seller name on the top navbar
    products=Products.objects.filter(seller_id =  request.session['seller'])
    return render(request,'seller_home.html',{'seller':seller,'product':products})

def add_product(request):

    message = ""
    if request.method == 'POST':  
        name = request.POST["pname"]
        price= request.POST["pprice"]
        description = request.POST["pdescription"]
        availability = request.POST["pquantity"]
        image = request.FILES["pimg"]
        seller = Seller.objects.get(seller_id=request.session['seller']) #taking all the object(row from table )

        new_product=Products(product_name=name,price=price,description=description,stock=availability,product_image=image,seller_id=seller)
        new_product.save()

        message="Sucessfully added the product"
    return render(request,'add_product.html',{'msg':message})

def view_product(request):  

    seller_product = Products.objects.filter(seller_id=request.session['seller'])  

    seller = Seller.objects.get(seller_id =  request.session['seller']) 
    return render(request,'view_product.html',{'products':seller_product,'sellers':seller})

def view_order(request):
    
    orders=Order.objects.filter(seller_id=request.session['seller'],status="ordered")
    
    return render(request,'view_order.html',{'order':orders,})

def change_password(request):

    msg=""    
    if request.method=="POST":
        old_psw=request.POST['oldpsw']
        new_psw=request.POST['newpsw']
        con_psw=request.POST['cpsw']

        seller_data=Seller.objects.get(seller_id=request.session['seller'])
        if old_psw==seller_data.seller_password:
            
            if new_psw==con_psw:
                seller_data.seller_password=new_psw #updation
                seller_data.save()
                msg="successfully change the password"
            else:
                msg="password mismatch"
        else:
            msg="password incorrect"



    return render(request,'change_password.html',{'msg':msg,})


def logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('common:sellerlogin')
