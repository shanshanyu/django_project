from django.db import models


# Create your models here.

class Department(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name='部门名称', max_length=50)


class Employee(models.Model):
    ''' 员工表 '''
    name = models.CharField(verbose_name='姓名', max_length=16)
    age = models.IntegerField(verbose_name='年龄')
    gender_choices = (
        (1,'男'),
        (2,'女')
    )
    # choices 是 python中的约束
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2)
    create_time = models.DateTimeField(verbose_name='入职时间',auto_now_add=True)
    # 级联删除
    #depart = models.ForeignKey(to='Department',to_field='id',on_delete=models.CASCADE)
    # 置空，to to_field 是数据库中的约束,外键约束
    depart = models.ForeignKey(to='Department',to_field='id',null=True,blank=True,on_delete=models.SET_NULL)