from django.db import models

# Create your models here.
class Data(models.Model):

    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)
    phonenumber=models.DecimalField(max_digits=10, decimal_places=0)
    password=models.CharField(max_length=20)
    aadharnumber=models.DecimalField(max_digits=12, decimal_places=0)
    age=models.PositiveSmallIntegerField()
    gender=models.CharField(max_length=1)

class Doctor(models.Model):
    name=models.CharField(max_length=10)
    weight=models.DecimalField(max_digits=3, decimal_places=2)
    bloodpressure=models.CharField(max_length=7)
    bloodgroup=models.CharField(max_length=3)
    past_disease=models.CharField(max_length=100)
    diagnosis=models.CharField(max_length=100)
    prescription=models.CharField(max_length=100)
    pass



