from django.http import HttpResponse
from django.shortcuts import render

from . import models

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")


def user_list(request):
    return render(request, 'user_list.html')

def user_add(request):
    return HttpResponse("新增用户")

def tpl(request):
    name = 'xiaoyumi'
    roles = ['admin', 'user', 'xx']
    return render(request,'tpl.html', {'name':name,'roles':roles})

#用户登录
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        print(request.POST)
        if request.POST.get('user') == 'admin' and request.POST.get('pwd') == '123':
            return HttpResponse('登录成功')
        else:
            return render(request, 'login.html',{'err_msg':'用户名或密码错误'})

def orm_insert(request):
    #插入数据到 app01_userinfo表中
    models.UserInfo.objects.create(username='xiaoyumi', password='1234')
    #删除这张表的所有数据
    # models.UserInfo.objects.all().delete()
    # #删除指定行
    # models.UserInfo.objects.filter(username='xiaoyumi').delete()
    return HttpResponse('成功')

def orm_select(request):
    data_list = models.UserInfo.objects.all()
    for item in data_list:
        print(item.username,item.password)

    data = models.UserInfo.objects.filter(username='xiaoyumi')
    for item in data:
        print(item.username,item.password)
    return HttpResponse('ok')


def orm_update(request):
    #把所有数据的密码改成111
    models.UserInfo.objects.all().update(password='111')
    #修改指定行
    models.UserInfo.objects.filter(username='xiaoyumi').update(password='123')
    return HttpResponse('ok')