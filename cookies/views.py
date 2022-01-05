import time

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime ,timedelta

# Create your views here.
from cookies import tasks
from cookies.models import Pic
from test1 import settings
from reportlab.pdfgen import canvas


def index(request):
    """设置cookies"""
    name = request.GET.get('name')
    respons = HttpResponse('设置cookie')
    respons.set_cookie('name', name, max_age=7*24*3600)
    respons.set_cookie('name', name, expires=datetime.now() + timedelta(days=14))
    return respons

def getcookies(request):
    """获取cookies"""
    cookie = request.COOKIES['name']
    return HttpResponse(cookie)


def setSession(request):
    name = request.GET.get('name')
    request.session['userName'] = name
    request.session.set_expiry(10) #10s过期

    return HttpResponse(name)


def getSession(request):
    userName = request.session['userName']
    return HttpResponse(userName)


def delSession(request):
    request.session.flush() # 清除session 表中的数据
    return HttpResponse('success')


def imgUpload(request):
    if(request.method =='GET'):
        return render(request, 'imgupload.html')
    else:
        f1 = request.FILES.get('pic')
        fname = '%s/images/%s' % (settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)


        Pic.objects.create(imgurl= ('images/%s' %f1.name))
        return HttpResponse('success')


def getImg(request):
    pic = Pic.objects.get(id=10)
    context={'pic':pic.imgurl}
    return render(request, 'showimg.html',context)


def pdf(request):
    """生成pdf文件"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    # 创建一个PDF对象，并使用响应对象作为它要处理的‘文件’
    p = canvas.Canvas(response)

    # 通过PDF对象的drawString方法，写入一条信息。具体参考模块的官方文档说明。
    p.drawString(100, 100, "Hello world.")
    # 关闭PDF对象
    p.showPage()
    p.save()
    return response


def sendeamil(request):
    msg = '<a href="https://lxldev.tech" target="_blank">进入</a>'
    send_mail('测试发送', '', settings.EMAIL_FROM,
              ['lxldevtest@163.com'],
              html_message=msg)
    return HttpResponse('ok')


def sayhello(request):
    print('hello ...')
    time.sleep(2)
    print('world ...')
    tasks.sayhello.delay()
    return HttpResponse("hello world")