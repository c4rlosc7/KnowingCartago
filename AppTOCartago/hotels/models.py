from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Modelo hoteles 

class Hotel(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	city = models.CharField(max_length=255)	
	phone = models.IntegerField(unique=True)
	email = models.EmailField(max_length=255)
	address = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=3)
	image = models.ImageField(blank=True)

# website = models.URLField()
# image = models.ImageField(blank=True)

# mostrar el campo que queremos en el admi
def __str__(self):
	return self.name

# funcion meta ordenar 
class Meta:
	ordering = ('id',)

