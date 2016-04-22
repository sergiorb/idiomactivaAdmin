from __future__ import unicode_literals

import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Class(models.Model):

	class Meta:
		verbose_name = _('Class')
		verbose_name_plural = _('Classes')

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=140, verbose_name=_('name'))
	max_students = models.PositiveIntegerField(default=1, verbose_name=_('max students'))

	def save(self):
		self.full_clean()
		super(Class, self).save()

	def __unicode__(self):
		return self.name

	def get_students(self):
		return " - ".join([str(p).decode('utf-8') for p in self.students.all()])
	get_students.short_description = _('students')

	def is_full(self):
		if self.students.all().count() < self.max_students:
			return False
		else:
			return True
	is_full.short_description = _('is full?')
	is_full.boolean = True

	def is_not_full(self):
		if self.students.all().count() < self.max_students:
			return True
		else:
			return False
	is_not_full.short_description = _('available')
	is_not_full.boolean = True

	def capacity(self):
		return '%s/%s' % (self.students.all().count(), self.max_students)
	capacity.short_description = _('capacity')
