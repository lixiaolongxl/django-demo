from django.urls import path

from cookies import views

urlpatterns=[
    path('index/', views.index),
    path('getcookies/', views.getcookies),
    path('setSession/', views.setSession),
    path('getSession/', views.getSession),
    path('delSession/', views.delSession),
    path('imgUpload/', views.imgUpload),
    path('getImg/', views.getImg),
    path('pdf/', views.pdf),
    path('sendeamil', views.sendeamil),
    path('sayhello', views.sayhello),
]