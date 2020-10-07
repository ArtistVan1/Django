from django.shortcuts import render
from django.http import HttpResponse
#处理http请求的代码
# Create your views here.
def listorders(request):
    return HttpResponse("下面是系统的所有订单")

def listorders1(request):
    return HttpResponse("下面是系统的所有订单111")


def listorders2(request):
    return HttpResponse("下面是系统的所有订单222")

def listorders3(request):
    return HttpResponse("下面是系统的所有订单333")