import datetime  
from django.db import models

from common.models import Customer, Seller
from sellers.models import Products

# Create your models here.

class Cart(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)

    class Meta:
        db_table='cart'

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    seller_id=models.ForeignKey(Seller,on_delete=models.CASCADE,default="")
    quantity=models.IntegerField()
    shipping_address=models.CharField(max_length=50)
    total_amount=models.FloatField()
    order_date=models.DateField(default=datetime.date.today)
    status=models.CharField(max_length=20,default="ordered")

    class Meta:
        db_table='orders'
