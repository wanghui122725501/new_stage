from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
# Create your views here.


def index(request):
    '''
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
    '''
    data = ["a","b","c"]
    data1 = {"aaa":"bbb","cccc":"dddd"}
    # return HttpResponse(json.dumps(data))  #返回普通的字符串类型
    # return JsonResponse(data,safe=False)   #如果数据类型是字典的话safe是True，是列表的话那safe=False
    return JsonResponse(data1)
    # return HttpResponse("hello world!!")
