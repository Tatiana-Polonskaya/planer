from django.urls import path,re_path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='schedule'),
]
