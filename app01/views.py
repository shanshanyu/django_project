from django.http import HttpResponse
from django.shortcuts import render

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