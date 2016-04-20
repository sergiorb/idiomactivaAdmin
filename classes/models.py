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

	def __unicode__(self):
		return self.name

	def get_students(self):
		return " - ".join([str(p) for p in self.students.all()])
	get_students.short_description = _('students')