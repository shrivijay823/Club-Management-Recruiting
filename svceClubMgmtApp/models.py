from unicodedata import name
from django.db import models

# Create your models here.
class Club(models.Model):
    name=models.CharField(max_length=30)
    logo_url=models.CharField(max_length=30)
    about=models.CharField(max_length=300)
    president_username=models.CharField(default='shri',max_length=30)
    recruiting=models.IntegerField(default=0)

class Volunteers(models.Model):
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    yos=models.IntegerField()
    sec=models.CharField(max_length=2)
    regno=models.CharField(max_length=10)
    phoneno=models.CharField(max_length=11)
    clgmailid=models.CharField(max_length=50)
    linkedin=models.CharField(max_length=100)
    clubname=models.CharField(default='no club',max_length=20)

    