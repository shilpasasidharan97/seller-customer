from ast import mod
from django.db import models

# Create your models here.


class Customer(models.Model):
    cust_id = models.AutoField(primary_key = True)
    cust_name = models.CharField(max_length = 20)
    cust_email = models.CharField(max_length = 20)
    cust_phone_no = models.CharField(max_length = 12)
    cust_password = models.CharField(max_length = 20)

# To set table name
    class Meta:  
        db_table = "customer"

class Seller(models.Model):
    seller_id = models.AutoField(primary_key = True)
    seller_name = models.CharField(max_length = 20)
    seller_email = models.CharField(max_length = 20)
    seller_phone_no = models.CharField(max_length = 12)
    account_holder = models.CharField(max_length = 20)
    account_number = models.CharField(max_length = 20)
    IFSC_code = models.CharField(max_length = 20)
    seller_password = models.CharField(max_length = 20)

    class Meta:
        db_table = "seller"