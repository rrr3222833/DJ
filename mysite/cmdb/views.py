# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render
from cmdb import  models
#user_list = [
 #   {"user":"jack","pwd":"abc"},
#    {"user":"tom","pwd":"ABC"},

#]

def index(request):
    #return HttpResponse("hello world!")
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        models.UserInfor.objects.create(user=username,pwd=password)
    user_list = models.UserInfor.objects.all()
        #print(username,password)
        #temp = {"user":username,"pwd":password}
        #user_list.append(temp)
    return  render(request,"index.html",{"data":user_list})
# Create your views here.
