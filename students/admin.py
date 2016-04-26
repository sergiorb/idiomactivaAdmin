from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportModelAdmin, ExportMixin

from .models import Adult, Student
from classes.models import Class


# Register your models here.


class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		exclude = ('id',)


	def clean(self):
		"""
		Checks that the selected class is not full-.
		"""

		classes = self.cleaned_data.get('classes')

		for a_class in classes:

			class_obj = Class.objects.get(pk=a_class.id)
			
			if not self.instance in class_obj.students.all():
			
				if a_class.is_full():
					raise ValidationError({
						'classes': ValidationError(_('%(value)s is full!'), params={'value': class_obj}, code='fullclass')
					})

		return self.cleaned_data


class AdultAdmin(ExportMixin, admin.ModelAdmin):

	fields = (
		'name',
		'surname_a',
		'surname_b',
		'born_date',
		'address',
		'phone',
		'mobile',
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
		'surname_b',
		'age',
		'born_date',
		'phone',
		'mobile',
		'email',
		'get_students',
	)
	
	list_filter = (
		#'age',
	)

	search_fields = (
		'name',
		'surname_a',
	)


class StudentAdmin(ExportMixin, admin.ModelAdmin):

	form = StudentForm

	fields = (
		'name', 
		'surname_a',
		'surname_b',
		'born_date',
		'address',
		'phone',
		'mobile',
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
		'school',
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