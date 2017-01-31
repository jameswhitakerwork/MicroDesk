from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(User, blank=True)

