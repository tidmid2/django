from django.db import models

class Tutorial(models.Model):
    first_name = models.CharField(max_length=100, blank=False, default='')
    last_name = models.CharField(max_length=100,blank=False, default='')
    email = models.CharField(max_length=100,blank=False, default=False)
    password = models.CharField(max_length=100,blank=False, default=False)
    status = models.IntegerField(default=1)