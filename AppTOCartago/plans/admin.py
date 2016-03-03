from django.contrib import admin

from .models import Plan
# Register your models here.

# permite mostrar en admin name y city
@admin.register(Plan)
class AdminPlan(admin.ModelAdmin):
	list_display = ('id', 'name', 'price',)
	list_filter = ('name', 'id',)