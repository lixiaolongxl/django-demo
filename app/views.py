import json

from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum, Max, Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from app.models import Student, AreaInfo


def index(request):
    print(request)

    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'request':request.GET
    })
    # return HttpResponse('index1')


def adds(request):
    # student = Student()
    # student.name = '李小龙'
    # # student.age = 20,
    # student.sex = True;
    # student.disc = '从事前端开发'
    # student.save()
    # studet = Student.object.all()
    studet = Student.object.create_s('刘德华',40,False,'唱歌')

    print(studet.name)
    return JsonResponse({
        'code' : 200,
        'msg' : 'success'
    })

def slist(request):
    """使用分页"""
    pIndex= request.GET.get('pagenum')
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    pSize = request.GET.get('pagesize')
    pSize = int(pSize)
    student = Student.objects.all()
    p = Paginator(student, pSize)

    # 获取第pIndex页的数据
    slist = p.page(pIndex)
    # print(list(slist.object_list.values()),type(list(slist.object_list.values())))

    # for i in slist.object_list:
    #     print(i.values())
    # json_data = serializers.serialize("json", slist, ensure_ascii=False)
    #
    # json_data_a = json.loads(json_data)

    # 获取所有的页码信息
    count = p.count
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'pagenum': pIndex,
        'count': count,
        'data':list(slist.object_list.values('name','age','sex'))
    })
    # lists = Student.objects.all().values('name','age')
    # lists = Student.objects.get(id__exact=1)
    # lists = Student.objects.filter()
    # 模糊查询
    # lists = Student.objects.filter(id__lte=3).values()
    # lists = Student.objects.all().order_by('-id').values()
    # Q对象
    # lists = Student.objects.filter(Q(id__lte=3)&Q(name='李小龙')).values()
    # lists = Student.objects.filter(Q(id=3)|Q(name='上上')).values()
    # lists = Student.objects.filter(~Q(id=3)).values()
    # 聚合
    # lists = Student.objects.filter(~Q(id=3)).aggregate(Count('id'))
    # lists = Student.objects.all().aggregate(Sum('id'))
    # lists = Student.objects.all().count()
    # lists = Student.objects.all().aggregate(Avg('id'))
    # print(lists)
    # print(lists['id__sum'])
    # for item in lists:
    #     print(item.id,item.name)
    # print(lists)
    # return JsonResponse({
    #     'code': 200,
    #     'data':'success'
    # })
    # return JsonResponse({
    #     'code': 200,
    #     'data': lists['id__sum']
    # })


def updates(request):
    student = Student.objects.get(pk=1)
    student.name='金城武'
    student.save()
    return JsonResponse({
        'code': 200,
        'msg': 'success'
    })


def deletes(request):
    try:
        student = Student.objects.get(pk=5)
        student.delete()
        return JsonResponse({
            'code': 200,
            'msg': 'success'
        })

    except Exception as err:
        return JsonResponse({
            'code': 500,
            'msg': '不存在'
        })

# 自关联
def getAreas(request):
    # air= AreaInfo.objects.get(atitle='广州市')
    # parent = air.aParent
    # list = air.areainfo_set.all()
    # print(list)

    lists = AreaInfo.objects.filter(aParent__atitle='河南省').values()
    # lists = AreaInfo.objects.filter(areainfo__atitle='河南省').values()
    arr=list(lists)


    # print(arr)
    return JsonResponse({
        'list':arr
    })