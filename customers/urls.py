from django.urls import path,include
from . import views

app_name = 'customers'

urlpatterns = [
    path('customerhome',views.customer_home,name='custhome'),
    path('viewcart',views.view_cart,name='cart'),
    path('vieworder',views.view_order,name='order'),
    path('changepsw',views.change_password,name="chngpsw"),
    path('cart/<int:id>',views.add_to_cart,name='addtocart'),
    path('logout',views.logout,name='logout'),
    path('order/<int:pid>',views.order,name='order'),
]





