from django.urls import path

from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('fibanocci', views.fibanocci, name='fibanocci'),
    path('result', views.result, name='result'),
]
