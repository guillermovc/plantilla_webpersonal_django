from django.contrib import admin
from .models import Project

# Al agregar cosas a este archivo, podemos extender las funcionalidades del panel de admin

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)