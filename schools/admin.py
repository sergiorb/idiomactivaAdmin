from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .models import School
from students.models import Student

# Register your models here.

class SchoolAdmin(ExportMixin, admin.ModelAdmin):

	fields = (
		'name',
		'address',
		'city',
		'info',
		'added_on',
	)

	readonly_fields = (
		'added_on',
	)

	list_display = (
		'name',
		'address',
		'city',
		'get_students',
	)

	list_filter = (
		'city',
	)

	search_fields = (
		'name',
		'address',
		'city',
	)

admin.site.register(School, SchoolAdmin)