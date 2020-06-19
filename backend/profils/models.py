from django.db import models
from datetime import datetime

topics_choices = (
    ('a', 'software engineering'),
    ('b', 'UI UX '),
)
skill_choices = (
    ('a', 'Hacker'),
    ('b', 'Hustler'),
    ('c', 'Hipster'),
)

major_choices = (
    ('a', 'FEB'),
    ('b', 'FIB'),
    ('c', 'FMIPA'),
    ('d', 'FISIPOL'),
    ('e', 'FT'),
)



class Profils(models.Model):
  

  avatar = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
  description = models.TextField(blank=True)
  chat = models.CharField(max_length=50, blank=True)
  linkedin = models.CharField(max_length=50, blank=True)
  about = models.CharField(max_length=50, blank=True)
  experience = models.CharField(max_length=50, blank=True)
  
  major = models.CharField(max_length=50, blank=True, choices= major_choices)
  skill = models.CharField(max_length=50, blank=True, choices=skill_choices)
  topics = models.CharField(max_length=50, blank=True, choices= topics_choices)
  
 