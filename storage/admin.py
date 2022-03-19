from django.contrib import admin
from .models import Category, File 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepolutated_fields = {'slug': ('name',)}


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
