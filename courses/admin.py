from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MaterialInLineAdmin(admin.TabularInline):
    model = Material


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

    inlines = [
        MaterialInLineAdmin
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Annoucement, Comment])
admin.site.register(Lesson, LessonAdmin)