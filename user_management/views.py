from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from . import models


def user_list(request):
    #获取用户列表
    data_list = models.User.objects.all()
    print(data_list)
    return render(request, 'new_user_list.html', {'data_list': data_list})

def add_user(request):
    # GET请求看到页面，POST请求提交数据
    if request.method == 'GET':
        return render(request, 'new_user_add.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 添加数据到数据库
    models.User.objects.create(username=username, password=password)
    #return HttpResponse('添加成功')
    # 自动跳到 user list
    return redirect('/new_user/list')


def del_user(request):
    username = request.GET.get('username')
    models.User.objects.filter(username=username).delete()
    #return HttpResponse('删除成功')
    # 自动跳到 user list
    return redirect('/new_user/list')