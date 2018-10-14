from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,QueryDict
import json
# Create your views here.


def index(request):

    print(request)
    print(request.scheme)
    print(request.method)
    print(request.META)
    print(request.body)
    print(request.path)
    print(request.path_info)
    print(request.encoding)
    print(request.GET)
    print(request.POST)

    data = ["a","b","c"]
    data1 = {"aaa":"bbb","cccc":"dddd"}
    # return HttpResponse(json.dumps(data))  #返回普通的字符串类型
    # return JsonResponse(data,safe=False)   #如果数据类型是字典的话safe是True，是列表的话那safe=False
    #return JsonResponse(data1)
    return HttpResponse("<h1>hello world!!</h1>"
                        "<h2>hello world</h2>")
# 总结
'''
视图函数
http.request
http.response
http.jsonresponse
自定义response（json.dumps）
'''

def index1(request):
    if request.method == "GET":
        print("GET:",request.GET)
        print("aa=",request.GET.get)
        print("bb=",request.GET.getlist)
    elif request.method == "POST":
        print("request POST=",request.POST)

    elif request.method == 'PUT':
        print("request PUT",QueryDict(request.body))

    elif request.method == "DELETE":
        print("request DELETE=",QueryDict(request.body))

    return HttpResponse("")
