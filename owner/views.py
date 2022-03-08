from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def new_seller(request):
    return render(request,'new_seller.html')

def customers(request):
    return render(request,'customers.html')

def sellers(request):
    return render(request,'sellers.html')