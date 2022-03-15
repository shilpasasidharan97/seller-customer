from django.urls import path
from . import views

app_name = 'sellers'

urlpatterns = [
    path('home',views.seller_home,name='sellerhome'),
    path('addproduct',views.add_product,name='addproduct'),
    path('viewproduct',views.view_product,name='viewproducts'),
    path('vieworders',views.view_order,name='vieworders'),
    path('changepsw',views.change_password,name='chngpsw'),
    path('logout',views.logout,name='logout'),
]