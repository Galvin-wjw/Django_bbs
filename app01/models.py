from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=64,unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    port = models.IntegerField(default=22)

    sys_type_choices = (
        ('linux',"LINUX"),
        ('win32',"WINDOWS")
    )
    sys_type = models.CharField(max_length=64,choices=sys_type_choices)
    idc = models.ForeignKey('IDC')
    groups = models.ManyToManyField('HostGroup')

    enabled = models.BooleanField(default=True)

    online_data = models.DateTimeField()
    create_data = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.hostname

class IDC(models.Model):
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class HostGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64,unique=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True,null=True)
    hosts = models.ManyToManyField('Host',blank=True,null=True)

    def __unicode__(self):
        return self.name
