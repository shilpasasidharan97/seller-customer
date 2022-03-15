import email
from tabnanny import check
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from common.forms import CustomerRegForm, SellerRegForm
from . models import * 

# Create your views here.

def home_page(request):
    return render(request,'home_page.html')

def seller_registration(request):
    
    msg=""
    form=SellerRegForm()

    if request.method == 'POST':
        form=SellerRegForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["seller_name"]
            email = form.cleaned_data["seller_email"]
            phone_no = form.cleaned_data["seller_phone_no"]
            account_holder = request.POST["account_holder"]
            account_number = request.POST["account_number"]
            ifsc = request.POST["IFSC_code"]
            password = request.POST["password"]

            email_exist = Seller.objects.filter(seller_email=email).exists()

            if not email_exist:
                new_seller = Seller(seller_name=name,seller_email=email,seller_phone_no=phone_no,account_holder=account_holder,account_number=account_number,IFSC_code=ifsc,seller_password=password)
                new_seller.save()
                form=SellerRegForm()
                msg= "Registration Completed"
            else:
                msg= "Email already taken"
        else:
            print(form.errors)
    return render(request,'seller_reg.html',{'msg':msg,'form':form})

def seller_login(request):

    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["psw"]

        seller_exist = Seller.objects.filter(seller_email=email,seller_password=password).exists()
        if seller_exist:
            seller_data = Seller.objects.get(seller_email=email,seller_password=password)
            request.session['seller'] = seller_data.seller_id
            return redirect('sellers:sellerhome')

        else:
            msg = "username or password is incorrect "
            return render(request,'seller_login.html',{'message':msg,})

    return render(request,'seller_login.html')

    

def customer_registration(request):
    msg = ""
    form=CustomerRegForm()
    if request.method == 'POST':
        form=CustomerRegForm(request.POST) #,request.FILES
        if form.is_valid():
            name=form.cleaned_data['cust_name']
            email = form.cleaned_data['cust_email']
            phone_number = form.cleaned_data['cust_phone_no']
            password =request.POST['cust_password']


            email_exist = Customer.objects.filter(cust_email=email).exists()# get multiple datads according to the where condition(select * from table where dep='it)

            if not email_exist:
                new_customer = Customer(cust_name=name,cust_email=email,cust_phone_no=phone_number,cust_password=password)
                new_customer.save() #insert into
                form=CustomerRegForm()
                msg= "Registration Completed"
            else:
                msg= "Email already taken"
        else:
            print(form.errors)
    return render(request,'customer_reg.html',{'message':msg,'form':form})


def customer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']

        customer_exist = Customer.objects.filter(cust_email=email,cust_password=password).exists()

        if customer_exist:
            customer_data = Customer.objects.get(cust_email=email,cust_password=password)
            request.session['customer'] = customer_data.cust_id
            return redirect('customers:custhome')

        else:    
            msg = "username or password is incorrect "
            return render(request,'customer_login.html',{'message':msg,})
    return render(request,'customer_login.html')


def check_customer_email(request):
    email=request.POST['email']
    customer_exist = Customer.objects.filter(cust_email=email).exists()
    if customer_exist:
        status=True
    else:
        status=False
    return JsonResponse({'status':status,'email':email})

