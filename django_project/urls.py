"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views as app01_views
from user_management import views as user_management_views
from employ_management import views as employ_management_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', app01_views.index),
    path('user/add/', app01_views.user_add),
    path('user/list/', app01_views.user_list),
    path('tpl/',app01_views.tpl),
    path('login/',app01_views.login),
    path('orm/insert/',app01_views.orm_insert),
    path('orm/select/',app01_views.orm_select),
    path('orm/update/',app01_views.orm_update),
    path('new_user/list/',user_management_views.user_list),
    path('new_user/add/',user_management_views.add_user),
    path('new_user/del/',user_management_views.del_user),
    path('depart/list/',employ_management_views.depart_list),
    path('depart/add/',employ_management_views.depart_add),
    path('depart/del/',employ_management_views.depart_del),
    path('depart/<int:nid>/edit/',employ_management_views.depart_edit),
]
