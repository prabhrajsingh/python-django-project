from django.contrib import admin

# Register your models here.
from .models import enter_detail

class detailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model', 'origin']
    search_fields = ['cylinders', 'horsepower', 'acceleration', 'model']

admin.site.register(enter_detail, detailsAdmin)