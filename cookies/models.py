from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=24)

    # class Meta:
    #     db_table = 'pyUser'  # 指定BookInfo生成的数据表名为bookinfo

class Pic(models.Model):
    """文件上传"""
    imgurl = models.ImageField(upload_to='images/')

