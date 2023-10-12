from django.db import models

# Create your models here.
class upload(models.Model):
    Name= models.CharField(max_length=30)
    Email= models.CharField(max_length=50)
    Phone= models.CharField(max_length=10)
    Image= models.FileField(upload_to="image")