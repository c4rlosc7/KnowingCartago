from django.contrib import admin

from .models import Hotel

# Register your models here.

#admin.site.register(Hotel)

# permite mostrar en admin name y city
@admin.register(Hotel)
class AdminHotel(admin.ModelAdmin):
	list_display = ('id', 'name', 'city',)
	list_filter = ('name', 'id',)
