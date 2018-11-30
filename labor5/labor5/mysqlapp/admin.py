from django.contrib import admin

from .models import Books


# Register your models here.

@admin.register(Books)
class IDKAdmin(admin.ModelAdmin):
    list_display = ['BookTitle', 'Description']
