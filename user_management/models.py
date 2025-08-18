from django.db import models

# Create your models here.


# 建表
class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)


