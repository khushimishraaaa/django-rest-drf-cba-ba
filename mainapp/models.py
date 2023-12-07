from django.db import models

# Create your models here.

class Teacher(models.Model):
    f_name = models.CharField(max_length=25, blank=False)
    l_name = models.CharField(max_length=50, blank=False)
    subject = models.CharField(blank=False,max_length=25)
    
   
    

