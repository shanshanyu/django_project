from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


# insert into 添加数据
# UserInfo.objects.create(username='小玉米',password='1234')
