from django.db import models

# Create your models here.

class Course(models.Model):
    cname = models.CharField(max_length=20)
    dur = models.IntegerField()
    fee = models.IntegerField()
    cdate = models.DateField(auto_now=True)
    trainer = models.CharField(max_length=25)

    def __str__(self):
        return self.cname
    
class Student(models.Model):
    sname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    portfolio = models.URLField(max_length=150)
    pic = models.ImageField(upload_to='media/app1/images')
    resume = models.FileField(upload_to='media/app1/files')
    join_date = models.DateField(auto_now=True)
    cname = models.ForeignKey("Course",on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

