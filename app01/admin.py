from django.contrib import admin

# Register your models here.

from app01 import models

admin.site.register(models.Host)
admin.site.register(models.HostGroup)
admin.site.register(models.IDC)
admin.site.register(models.UserProfile)