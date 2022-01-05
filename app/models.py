from django.db import models

class StudentManage(models.Manager):
    def all(self):
        return super().all().filter(sex=True)

    def create_s(self, name,age,sex,disc):
        student = self.model()
        student.name = name
        student.age = age
        student.sex = sex
        student.disc = disc
        student.save()
        return student

class Student(models.Model):
    """学生类"""
    name = models.CharField(max_length=16)
    age = models.IntegerField(default=0)
    sex = models.BooleanField(default=True)
    disc = models.TextField(max_length=1200)
    objects= StudentManage()

class NewsType(models.Model):
    typeName = models.CharField(max_length=20)

class NewsInfo(models.Model):
    title=models.CharField(max_length=20)
    update= models.DateTimeField(auto_now_add=True)
    content= models.TextField(max_length=4000)
    news_type=models.ManyToManyField('NewsType')
class BaseInfo(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    gender=models.BooleanField(default=False)

class Info(models.Model):
    address= models.CharField(max_length=120)
    photo=models.CharField(max_length=400)
    base_info=models.OneToOneField('BaseInfo',on_delete=models.CASCADE)

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=16)
    aParent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'area'  # 指定BookInfo生成的数据表名为bookinfo






