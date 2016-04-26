from django.contrib import admin
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):

	site_header = 'Idiomactiva'
	index_template = "admin/index.html"

admin_site = MyAdminSite(name='myadmin')
