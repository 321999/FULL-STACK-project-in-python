from django.db import models

# Create your models here.
# each field  is specified as a class attribute and each attribute is the tables column 
# class Student(models.Model):
   
   
#     name=models.CharField(max_length=30)
#     roll=models.IntegerField()
#     email=models.EmailField()
#     marks=models.IntegerField()
#     address=models.CharField(max_length=100)
   
# creating the prouduct schema 
# class Product(models.Model):
#     name=models.CharField(max_length=30)
#     email=models.EmailField(null=True,blank=True)
#     star=models.IntegerField(null=True,blank=True)
#     loc=models.CharField(max_length=100)


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True,blank=True)
    age=models.IntegerField()
    address=models.TextField(null=True,blank=True)