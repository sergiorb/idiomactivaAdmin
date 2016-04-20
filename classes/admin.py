from django.contrib import admin

from .models import Class
from students.models import Student

# Register your models here.

class StudentshipInline(admin.TabularInline):
    model = Student.classes.through


class ClassAdmin(admin.ModelAdmin):

	fields = (
		'name', 
	)

	list_display = (
		'name',
		'get_students',
	)

	search_fields = (
		'name',
	)

	inlines = [
		StudentshipInline,
	]

admin.site.register(Class, ClassAdmin)