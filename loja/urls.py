from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.base, name='base'),
    path('', views.blank, name='blank'),
    path('', views.charts, name='charts'),
    path('', views.password, name='password'),
    path('', views.login, name='login'),
    path('', views.register, name='register'),
    path('', views.tables, name='tables'),
    path('', views.erro, name='erro'),
]