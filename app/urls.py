from django.urls import path

from app import views

urlpatterns=[
    path('index/', views.index),
    path('adds', views.adds),
    path('slist', views.slist),
    path('updates', views.updates),
    path('deletes', views.deletes),
    path('getAreas', views.getAreas),

]