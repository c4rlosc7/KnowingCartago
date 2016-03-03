from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phone = models.IntegerField(unique=True)
	city = models.CharField(max_length=255)	
	
# admin board
def __str__(self):
	return self.name

# meta ordenar 
class Meta:
	ordering = ('id',)