from django.urls import path, include
from . import views

app_name = 'state'

urlpatterns = [
    path('index',views.index,name='dropdown'),
    path('statecheck',views.state_check,name='statecheck')
]