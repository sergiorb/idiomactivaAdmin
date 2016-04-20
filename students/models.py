from __future__ import unicode_literals

import uuid

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
	age = models.PositiveIntegerField(default=0, verbose_name=_('age'))
	address = models.CharField(max_length=140, verbose_name=_('address'))
	phone = models.CharField(max_length=140, verbose_name=_('phone'))
	email = models.EmailField(max_length=254, verbose_name=_('email'))
	info = models.TextField(blank=True, null=True, verbose_name=_('info'))
	added_on = models.DateTimeField(default=timezone.now, verbose_name=_('added on'))

	def __unicode__(self):
		return '%s %s' % (self.name, self.surname_a)


class Adult(Person):

	class Meta:
		verbose_name = _('Adult')
		verbose_name_plural = _('Adults')


class Student(Person):

	class Meta:
		verbose_name = _('Student')
		verbose_name_plural = _('Students')

	school = models.ForeignKey(School, related_name='students', blank=True, null=True, verbose_name=_('school'))
	adults = models.ManyToManyField(Adult, related_name='students', blank=True, null=True, verbose_name=_('adults'))
	classes = models.ManyToManyField(Class, related_name='students', blank=True, null=True, verbose_name=_('classes'))