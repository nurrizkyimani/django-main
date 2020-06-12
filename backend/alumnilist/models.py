from django.db import models

# Create your models here.
class Alumni(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=100)

  def __str__(self):
    return self.email