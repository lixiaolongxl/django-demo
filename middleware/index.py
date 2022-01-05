from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin

class Mymid(MiddlewareMixin):
    # def __init__(self):
    #     pass
    def process_request(self, request):
        print(request.path)
        """处理请求前：在每个请求上，request对象产生之后，url匹配之前调用，返回None或HttpResponse对象。"""
        # print(request.META.get('REMOTE_ADDR'))
        pass

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """处理视图前：在每个请求上，url匹配之后，视图函数调用之前调用，返回None或HttpResponse对象"""
        # print('--------------view')
        pass

    def process_response(self, request, response):
        """处理响应后：视图函数调用之后，所有响应返回浏览器之前被调用，在每个请求上调用，返回"""
        # print('--------------response')
        return response

    def process_exception(self, request, exception):
        """异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象"""

        return HttpResponse(exception)
        # pass