import email
from tabnanny import check
from unicodedata import name
from django.shortcuts import redirect, render
from . models import * 

# Create your views here.

def home_page(request):
    return render(request,'home_page.html')

def seller_registration(request):
    
    msg=""

    if request.method == 'POST':
        name = request.POST["seller_name"]
        email = request.POST["seller_email"]
        phone_no = request.POST["seller_phn"]
        account_holder = request.POST["seller_acc_holder"]
        account_number = request.POST["seller_accno"]
        ifsc = request.POST["ifsc"]
        password = request.POST["seller_psw"]

        email_exist = Seller.objects.filter(seller_email=email).exists()

        if not email_exist:
            new_seller = Seller(seller_name=name,seller_email=email,seller_phone_no=phone_no,account_holder=account_holder,account_number=account_number,IFSC_code=ifsc,seller_password=password)
            new_seller.save()
            msg= "Registration Completed"
        else:
            msg= "Email already taken"
           
    return render(request,'seller_reg.html',{'msg':msg,})

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
    if request.method == 'POST':
        name = request.POST['cname']
        email = request.POST['cemail']
        phone_number = request.POST['cphoneno']
        password = request.POST['cpsw'] 

        email_exist = Customer.objects.filter(cust_email=email).exists()

        if not email_exist:
            new_customer = Customer(cust_name=name,cust_email=email,cust_phone_no=phone_number,cust_password=password)
            new_customer.save()
            msg= "Registration Completed"
        else:
            msg= "Email already taken"
    return render(request,'customer_reg.html',{'message':msg,})


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