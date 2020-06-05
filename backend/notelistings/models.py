from django.db import models
from skilltors.models import Skilltor
# Create your models here.

class Note(models.Model):
  class SalesType(models.Model):
    FOR_SALE = 'for sale'
    FOR_FREE = 'for free usage'
    FOR_SOLD = 'SOLD'


  skilltors = models.ForeignKey(Skilltor, on_delete=models.DO_NOTHING)
  slug = models.CharField(max_length=100, unique=True)
  title  = models.CharField(max_length=50)
  instructor = models.CharField(max_length=50)
  semester = models.CharField( max_length=50)
  year = models.CharField(max_length=50)
  course = models.CharField(_max_length=50)
  description = models.TextField(blank=True)
  upload_date = models.DateField(auto_now=True, auto_now_add=False)

  sale_type= models.models.CharField( max_length=50, choices=SalesType.choices, default= SalesType.FOR_SALE)

  photo_main = models.ImageField( upload_to='%photos/%Y/%m/%d')
  photo_1 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_2 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_3 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_4 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_5 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  photo_6 = models.ImageField( upload_to='%photos/%Y/%m/%d', blank=True)
  