from django.urls import path

from redisTest import views

urlpatterns=[
    path('index/', views.index),
    path('setssion/', views.setssion),
    path('getsession/', views.getsession)
]