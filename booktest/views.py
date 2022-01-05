from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import json


# Create your views here.
# def index(request):
#     return JsonResponse({
#         'code': 200,
#         'msg': 'success',
#         'request': request.GET
#     });

class BookList(View):
    def get(self, request):
        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'request': request.GET
        });

    def post(self, request):
        postBody = request.body
        # print(postBody)
        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'response': json.loads(postBody)
        }, safe=False);
