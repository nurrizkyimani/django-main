from django.db import models

# Create your models here.

class Note(models.Model):
  id = models.CharField( max_length=50)
  title  = models.CharField( max_length=50)
  instructor = models.CharField(max_length=50)
  semester = models.CharField( max_length=50)
  year = models.CharField(max_length=50)
  course = models.CharField(_max_length=50)
  description = models.TextField(blank=True)
  upload_date = models.DateField(auto_now=True, auto_now_add=False)
  photo_main = models.ImageField( upload_to='%photos/%Y/%m/%d')
  photo_1 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_2 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_3 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_4 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_5 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_6 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  