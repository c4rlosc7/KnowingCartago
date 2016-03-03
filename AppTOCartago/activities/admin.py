from django.contrib import admin
from .models import Activity
# Register your models here.

# permite mostrar en admin name y city
@admin.register(Activity)
class AdminActivity(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'price', 'image',)
	list_filter = ('name', 'id',)