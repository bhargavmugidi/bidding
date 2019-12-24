from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from user.models import RegisterModel

def check_admin(request):
    username = request.POST["a1"]
    password = request.POST["a2"]
    if username == "admin" and password == "admin":
        return redirect("admin_home")
    else:
        messages.error(request,"Invalid Details")
        return redirect("admin_login")


def pendingReg(request):
    qs = RegisterModel.objects.filter(status="pending")
    return render(request,"badmin_template/pending_reg.html",{"data":qs})