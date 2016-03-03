from django.contrib import admin
from .models import Contact
# Register your models here.

# permite mostrar en admin name y city
@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'phone', 'city',)
	list_filter = ('name', 'id',)