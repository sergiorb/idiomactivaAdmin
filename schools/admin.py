from django.contrib import admin

from .models import School

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):

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