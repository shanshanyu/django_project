from django.shortcuts import render,redirect
from . import models
# Create your views here.


def depart_list(request):
    ''' 部门列表 '''
    data_list = models.Department.objects.all()
    return render(request, 'depart_list.html', {'data_list': data_list})


def depart_add(request):
    ''' 添加部门 '''
    if request.method == "GET":
        return render(request,'depart_add.html')
    depart = request.POST.get('title')
    models.Department.objects.create(title=depart)
    return redirect('/depart/list')


def depart_del(request):
    ''' 删除部门 '''
    #获取部门
    depart = request.GET.get('nid')
    #删除部门
    models.Department.objects.filter(id=depart).delete()
    return redirect('/depart/list')


def depart_edit(request,nid):
    if request.method == "GET":
        # depart通过 depart_list中的编辑按钮传递过来的参数
        depart = models.Department.objects.get(id=nid)
        return render(request,'depart_edit.html',{'depart':depart})
    #获取到用户输入的部门
    depart = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=depart)
    return redirect('/depart/list')

