from __future__ import unicode_literals

from django.db import models
from hr.models import Program

from django.utils import timezone
import datetime
from datetime import timedelta

# Create your models here.

class Report(models.Model):
    program = models.ForeignKey(Program)
    deadline = models.DateField()
    reportee = models.EmailField()
    name = models.CharField(max_length=64)
    report = models.FileField(upload_to='reports/',blank=True)

    def time_left(self):
        t = timezone.now().date()
        d = self.deadline
        days_left = d - t
        return days_left

    def days_left(self):
        t = self.time_left()
        days = t.days
        return days

    def __unicode__(self):
        return self.program.__unicode__() + ' - ' + self.name 

    class Meta:
        permissions = (
            ('download_reports', 'Can Download Reports'),
        )
