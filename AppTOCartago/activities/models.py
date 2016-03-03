from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Activity(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=9, decimal_places=3)
	image = models.ImageField(blank=True)
	
# admin board
def __str__(self):
	return self.name

# meta ordenar 
class Meta:
	ordering = ('id',)