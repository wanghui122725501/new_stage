from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    username_q = 'admin'
    password_q = '123456'
    if request.method == "POST":
        print(request.POST)
        print("username",request.POST.get('username'))
        if request.POST.get('username') == username_q and request.POST.get('password') == password_q:
            print("success")
            return HttpResponse("登陆成功")
        else:
            print("failed")
            return HttpResponse("登录失败")