from django.db import models

# Create your models here.
class user(models.Model):
    Username= models.CharField(max_length=30)
    First= models.CharField(max_length=30)
    Last= models.CharField(max_length=30)
    Email= models.CharField(max_length=50)
    Password= models.CharField(max_length=128)
    Confirm= models.CharField(max_length=128)

class log(models.Model):
    Username= models.CharField(max_length=30)
    Password= models.CharField(max_length=128)

class first(models.Model):
    Title=models.CharField(max_length=60)
    Content=models.CharField(max_length=2000)

class ne(models.Model):
    Blogtitle=models.CharField(max_length=60)
    Blogcontent=models.CharField(max_length=2000)

class colb(models.Model):
    Colltitle=models.CharField(max_length=60)
    Collcontent=models.CharField(max_length=2000)