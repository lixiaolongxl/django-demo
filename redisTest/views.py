from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('index')


def setssion(request):
    request.session['userName']='lxlxiaolong'
    request.session['age']=18
    return HttpResponse('设置session')


def getsession(request):
    username =  request.session['userName']
    age = request.session['age']
    return HttpResponse(username + str(age))