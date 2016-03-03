from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Reservation(models.Model):
	name = models.CharField(max_length=255)
	checkin = models.DateField()
	checkout = models.DateField()	
	phone = models.IntegerField(unique=True)
	room = models.IntegerField()	
	
# admin board
def __str__(self):
	return self.name

# meta ordenar 
class Meta:
	ordering = ('id',)