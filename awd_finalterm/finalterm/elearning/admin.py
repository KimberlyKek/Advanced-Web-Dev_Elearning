from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_type', 'course_name', 'course_outline')

class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('course_type',)

class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email','status','role')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    list_display = ('username','first_name','last_name','email','role')

admin.site.register(User, UserAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Course_Type, CourseTypeAdmin) 


