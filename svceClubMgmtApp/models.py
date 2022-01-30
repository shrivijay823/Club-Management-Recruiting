from unicodedata import name
from django.db import models

# Create your models here.
class Club(models.Model):
    name=models.CharField(max_length=30)
    logo_url=models.CharField(max_length=30)
    about=models.CharField(max_length=300)
    president_username=models.CharField(max_length=30)
    recruiting=models.IntegerField(default=0)
    