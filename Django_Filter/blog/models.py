# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import URLValidator

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=20,null=True, blank=True )
    domain = models.TextField(validators=[URLValidator()])

    image = models.FileField(upload_to='media/',null = True, blank=True)

    reviews = models.IntegerField(default=0)
    discription = models.TextField(max_length=500, blank=True)
    tags = models.TextField(max_length=100,null=True, blank=True )
    categories = models.CharField(max_length=20,null=True, blank=True )
    city = models.CharField(max_length=20,null=True, blank=True )
    sub_loc = models.CharField(max_length=20,null=True, blank=True )
    popularity = models.IntegerField(default=0)
    trending = models.IntegerField(default=0)
    
    

    def __str__(self):
        return str(self.name)

