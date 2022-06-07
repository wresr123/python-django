from django.db import models

# Create your models here.

class Client(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20, default=None, null=True)
    name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=11)
    company = models.CharField(max_length=20)
    position = models.CharField(max_length=15)

    signed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Manufacturer(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20, default=None, null=True)
    name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=11)
    company = models.CharField(max_length=20)

    signed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



