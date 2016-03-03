
from django.contrib import admin

from .models import Transport

# Register your models here.

#admin.site.register(Hotel)

# permite mostrar en admin name y city
@admin.register(Transport)
class AdminTransport(admin.ModelAdmin):
	list_display = ('id', 'name', 'city',)
	list_filter = ('name', 'id',)