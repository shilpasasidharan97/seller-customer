from django.urls import path,include
from . import views

app_name = 'customers'

urlpatterns = [
    path('customerhome',views.customer_home,name='custhome'),
    path('viewcart',views.view_cart,name='cart'),
    path('vieworder',views.view_order,name='order'),
]