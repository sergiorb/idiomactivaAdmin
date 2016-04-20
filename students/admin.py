from django.contrib import admin

from .models import Adult, Student

# Register your models here.


class AdultAdmin(admin.ModelAdmin):

	fields = (
		'name', 
		'surname_a',
		'surname_b',
		#'age',
		'born_date',
		'address',
		'phone',
		'email',
		'info',
		'added_on',
	)

	readonly_fields = (
		'added_on',
	)

	list_display = (
		'name',
		'surname_a',
		'age',
		'email',
		'born_date',
	)
	
	list_filter = (
		#'age',
	)

	search_fields = (
		'name',
		'surname_a',
	)


class StudentAdmin(admin.ModelAdmin):


	fields = (
		'name', 
		'surname_a',
		'surname_b',
		'born_date',
		'address',
		'phone',
		'email',
		'info',
		'school',
		'adults',
		'classes',
		'added_on',
	)

	readonly_fields = (
		'added_on',
	)

	list_display = (
		'name',
		'surname_a',
		'surname_b',
		'age',
		'born_date',
		'phone',
		'mobile',
		'email',
		'get_classes',
		'get_adults',
	)

	list_filter = (
		#'age',
	)

	search_fields = (
		'name',
		'surname_a',
		'surname_b',
	)



admin.site.register(Adult, AdultAdmin)
admin.site.register(Student, StudentAdmin)