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
