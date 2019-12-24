from django.db import models


class RegisterModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    doj = models.DateField(auto_now_add=True)

