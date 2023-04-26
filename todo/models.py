from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    #id auto-increment primary key
    title=models.CharField(max_length=100)
    text=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    date_completed=models.DateField(null=True,blank=True)
    important=models.BooleanField(default=False)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE) 

    def  __str__(self): #self 取得自己本身的模組
        return f'{self.title}-\
            {self.created.strftime("%Y-%m-%d %H:%M:%S")}' #回傳列表的title , created


class student(models.Model):
    cName = models.CharField(max_length=20,null=False)
    cSex = models.CharField(max_length=2, default="M", null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank= True, default="")
    cPhone = models.CharField(max_length=50, blank=True, default="")
    cAddr = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.cName