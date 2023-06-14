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
    
