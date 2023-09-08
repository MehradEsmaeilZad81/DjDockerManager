from django.contrib import admin
from .models import App

# Register your models here.


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'command')
    list_filter = ('name', 'image')
    search_fields = ('name', 'image')
    ordering = ('name',)
