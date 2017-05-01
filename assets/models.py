from __future__ import unicode_literals

from django.db import models
from hr.models import Office, Staff, Program

from django.utils import timezone


# Create your models here.

class AssetType(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Asset(models.Model):
    STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'inactive'),
        ('destroyed', 'destroyed'),
        ('lost', 'lost'),
    )

    no = models.IntegerField(unique=True)
    sub_no = models.IntegerField(blank=True)
    capitalized = models.DateField()
    descr = models.ForeignKey(AssetType)
    add_descr = models.CharField(max_length=256, blank=True)
    serial = models.CharField(max_length=128, blank=True)
    office = models.ForeignKey(Office)
    program = models.ForeignKey(Program)
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='active',
        blank=True,
        max_length=32
    )

    def assigned(self):
        c = Check.objects.filter(asset=self).order_by('-date').first()
        if c:
            if c.check_type == 'out':
                return c.staff
        else:
            return None

    def __unicode__(self):
        return str(self.no) + ': ' + self.descr.name

    class Meta:
        permissions = (
            ("can_download_assets", "Can Download Assets"),
        )


class Check(models.Model):
    CHECK_CHOICES = (
        ('in', 'in'),
        ('out', 'out')
    )
    asset = models.ForeignKey(Asset)
    staff = models.ForeignKey(Staff)
    date = models.DateField(default=timezone.now())
    check_type = models.CharField(choices=CHECK_CHOICES, max_length=8)
    document = models.FileField(upload_to='assets/')


