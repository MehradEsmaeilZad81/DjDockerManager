from django.contrib import admin
from .models import App, Run

# Register your models here.


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'command')
    list_filter = ('name', 'image')
    search_fields = ('name', 'image')
    ordering = ('name',)


@admin.register(Run)
class AppAdmin(admin.ModelAdmin):
    list_display = ('app', 'start_time', 'status')
    list_filter = ('app', 'start_time', 'status')
    search_fields = ('app', 'start_time', 'status')
    ordering = ('app', 'start_time', 'status')
