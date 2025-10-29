from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
# Create your models here.
class User(models.Model): # position table
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    

# primary key will create by yrm ID will create.