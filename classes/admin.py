import re

from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms.models import BaseInlineFormSet

from import_export.admin import ImportExportModelAdmin, ExportMixin
from .models import Class
from students.models import Student


class ClassForm(forms.ModelForm):
	class Meta:
		model = Class
		exclude = ('id',)

	def clean(self):
		
		max_students = self.cleaned_data.get('max_students')
		students_count = self.instance.students.all().count()
		
		if students_count > max_students:
			raise ValidationError({
				'max_students': ValidationError(_('Max students has to be equal or greater than current assigned students'), code='invalid-number')
				})

		"""
		students_ids = []
		
		for data in self.data:
			if re.match(r'Student_classes-\d+-student', data, flags=0):
				if self.data[data] not in students_ids:
					students_ids.append(self.data[data])

		print self.cleaned_data

		adding = 0
		for students_id in students_ids:
			student_obj = Student.objects.get(pk=str(students_id))
			if not student_obj in self.instance.students.all():
				adding += 1

		print adding

		if len(students_ids) > max_students:
			raise ValidationError(
				ValidationError(_('There is not enough space in this class!!'), 
				code='invalid-number')
			)
		"""

		return self.cleaned_data



class StudentshipInlineFormSet(BaseInlineFormSet):
	def clean(self):
		super(StudentshipInlineFormSet, self).clean()
		adding_students = 0
		for form in self.forms:
			if not form.is_valid():
				return #other errors exist, so don't bother
			if form.cleaned_data and not form.cleaned_data.get('DELETE'):
				adding_students += 1

		max_students = 0		
		for data in self.cleaned_data:
			if data.get('class'):
				max_students = data.get('class').max_students
				break

		if adding_students > max_students:
			raise ValidationError(
				ValidationError(_('There is not enough space in this class!!'), 
				code='invalid-number')
			)

class StudentshipInline(admin.TabularInline):
	model = Student.classes.through
	formset = StudentshipInlineFormSet


class ClassAdmin(ExportMixin, admin.ModelAdmin):

	form = ClassForm
	fields = (
		'name',
		'max_students',
	)

	list_display = (
		'name',
		'is_not_full',
		'capacity',
		'get_students',
	)

	search_fields = (
		'name',
	)

	inlines = [
		StudentshipInline,
	]

admin.site.register(Class, ClassAdmin)