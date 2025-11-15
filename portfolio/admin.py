from django.contrib import admin
from .models import (Profile, SkillCategory, Skill, Project, Technology, 
                     Experience, Education, Testimonial, BlogPost, ContactMessage)


class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'available_for_hire')
    list_editable = ('available_for_hire',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'bio', 'profile_image', 'profile_image_url', 'resume_file', 'available_for_hire')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'stackoverflow_url', 'medium_url')
        }),
    )


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'icon')
    list_editable = ('order',)
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_editable = ('order', 'proficiency')
    list_filter = ('category',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'is_current', 'order')
    list_editable = ('order',)
    list_filter = ('start_date',)
    fieldsets = (
        ('Position Information', {
            'fields': ('company', 'position', 'location')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date')
        }),
        ('Details', {
            'fields': ('description', 'technologies', 'order')
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    list_filter = ('start_date',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'stage', 'featured', 'order', 'created_at')
    list_editable = ('order', 'featured')
    list_filter = ('stage', 'featured')
    inlines = [TechnologyInline]
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'stage', 'description', 'image', 'featured', 'order')
        }),
        ('Problem & Solution', {
            'fields': ('problem_statement', 'solution_approach'),
            'classes': ('collapse',)
        }),
        ('Technical Details', {
            'fields': ('technical_architecture', 'design_decisions', 'testing_strategy'),
            'classes': ('collapse',)
        }),
        ('Links', {
            'fields': ('project_url', 'github_url', 'api_documentation_url')
        }),
    )


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'order')
    list_filter = ('project',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company', 'is_active', 'order', 'created_at')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active', 'created_at')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at', 'updated_at')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'featured_image', 'tags')
        }),
        ('Publishing', {
            'fields': ('published',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'read')
    list_editable = ('read',)
    list_filter = ('read', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
