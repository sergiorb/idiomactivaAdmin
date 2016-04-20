from __future__ import unicode_literals

import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class School(models.Model):

	class Meta:
		verbose_name = _('School')
		verbose_name_plural = _('Schools')

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	added_on = models.DateTimeField(default=timezone.now, verbose_name=_('added on'))
	info = models.TextField(blank=True, null=True, verbose_name=_('info'))
	name = models.CharField(max_length=140, verbose_name=_('name'))
	address = models.CharField(max_length=140, blank=True, null=True, verbose_name=_('address'))
	city = models.CharField(max_length=140, verbose_name=_('city'))

	def __unicode__(self):
		return '%s - %s ' % (self.name, self.city)
