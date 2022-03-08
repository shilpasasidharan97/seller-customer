from unicodedata import name
from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('home',views.home,name="homepage"),
    path('newseller',views.new_seller,name='newseller'),
    path('customer',views.customers,name='custm'),
    path('sellers',views.sellers,name='seller')
]