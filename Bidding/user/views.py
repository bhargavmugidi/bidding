from django.shortcuts import render,redirect
from .models import RegisterModel
from django.contrib import messages

def registerUser(request):
    name = request.POST["s1"]
    contact = request.POST["s2"]
    email = request.POST["s3"]
    password = request.POST["s4"]
    status = "pending"
    RegisterModel(name=name,contact=contact,email=email,password=password,status=status).save()
    messages.success(request,"Registration Need to Approve By Admin")
    return redirect("buyer_seller")