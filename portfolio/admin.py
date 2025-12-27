from django.contrib import admin
from .models import Project, Service, Experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'tech_stack', 'created_at', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description', 'tech_stack']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'current']
    list_filter = ['current']
