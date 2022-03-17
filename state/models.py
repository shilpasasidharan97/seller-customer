from django.db import models

# Create your models here.

class State(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=20)

    class Meta:
        db_table='states'

class District(models.Model):
    dist_id=models.AutoField(primary_key=True)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE)
    dist_name=models.CharField(max_length=20)
    class Meta:
        db_table='district'