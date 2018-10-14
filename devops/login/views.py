from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate

# Create your views here.

def loginTest(request):
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

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        userpass = request.POST.get('userpass')
        user = authenticate(request,username=username,password=userpass)
        if user is not None:
            login(request,user)
            return HttpResponse("用户登录成功！")
        else:
            return HttpResponse("用户登录失败！")
    return render(request,'user_login.html')
