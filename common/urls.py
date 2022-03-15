from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('',views.home_page,name='homepage'),
    path('sellerregistration',views.seller_registration,name='sellerregistration'),
    path('sellerlogin',views.seller_login,name='sellerlogin'),
    path('cusreg',views.customer_registration,name='reg'),
    path('customerlogin',views.customer_login,name='customlogin'),
    path('checkcustemail',views.check_customer_email,name='checkmail'),
]