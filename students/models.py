from __future__ import unicode_literals

import uuid
from datetime import date

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from schools.models import School
from classes.models import Class


# Create your models here.


class Person(models.Model):

	class Meta:
		abstract = True

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=140, verbose_name=_('name'))
	surname_a = models.CharField(max_length=140, verbose_name=_('surname'))
	surname_b = models.CharField(max_length=140, blank=True, null=True, verbose_name=_('surname b'))
	born_date = models.DateField(null=True, verbose_name=_('date of birth'))
	address = models.CharField(max_length=140, verbose_name=_('address'))
	phone = models.CharField(max_length=140, blank=True, null=True, verbose_name=_('phone'))
	mobile = models.CharField(max_length=140, blank=True, null=True, verbose_name=_('mobile'))
	email = models.EmailField(max_length=254, blank=True, null=True, verbose_name=_('email'))
	info = models.TextField(blank=True, null=True, verbose_name=_('info'))
	added_on = models.DateTimeField(default=timezone.now, verbose_name=_('added on'))

	def __unicode__(self):
		return '%s %s' % (self.name, self.surname_a)

	def age(self):
		# THANKS TO: http://stackoverflow.com/a/9754466

		if self.born_date != None:

			today = date.today()
			return today.year - self.born_date.year - ((today.month, today.day) < (self.born_date.month, self.born_date.day))

		else:
			return None
	age.short_description = _('age')


class Adult(Person):

	class Meta:
		verbose_name = _('Adult')
		verbose_name_plural = _('Adults')

	def get_students(self):
		return " - ".join([str(p).decode('utf-8') for p in self.students.all()])
	get_students.short_description = _('students')


class Student(Person):

	class Meta:
		verbose_name = _('Student')
		verbose_name_plural = _('Students')
	school = models.ForeignKey(School, on_delete=models.PROTECT, related_name='students', blank=True, null=True, verbose_name=_('school'))
	adults = models.ManyToManyField(Adult, related_name='students', blank=True, null=True, verbose_name=_('adults'))
	classes = models.ManyToManyField(Class, related_name='students', blank=True, null=True, verbose_name=_('classes'))

	def get_classes(self):
		return " - ".join([str(p) for p in self.classes.all()])
	get_classes.short_description = _('classes')

	def get_adults(self):
		return " - ".join([str(p) for p in self.adults.all()])
	get_adults.short_description = _('adults')