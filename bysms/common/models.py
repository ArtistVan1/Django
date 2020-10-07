from django.db import models
#存放数据库对象
# Create your models here.
class Customer(models.Model):
    #name
    name = models.CharField(max_length=200) #varchar
    #telephone num
    phonenumber = models.CharField(max_length=200)
    #address
    address = models.CharField(max_length=200)
    #line
    line = models.CharField(max_length=30,null=True,blank=True)