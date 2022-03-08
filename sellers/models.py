from distutils.command.upload import upload
from django.db import models

from common.models import Seller

# Create your models here.

class Products(models.Model):
    p_id = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_name =  models.CharField(max_length=20)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.IntegerField()
    product_image = models.ImageField(upload_to = 'products/')

    class Meta:
        db_table = 'products'