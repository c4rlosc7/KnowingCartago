from django.contrib import admin
from .models import Reservation
# Register your models here.

# permite mostrar en admin name y city
@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
	list_display = ('id', 'name', 'checkin', 'checkout', 'phone', 'room',)
	list_filter = ('name', 'id',)