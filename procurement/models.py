from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from hr.models import Staff, Department, Mission, Office, Program
from jsignature.mixins import JSignatureFieldsMixin
from django.utils import timezone
import decimal

# Create your models here.

class PRStatus(models.Model):
    status = models.CharField(max_length=32)

class JSignatureModel(JSignatureFieldsMixin):
    name = models.CharField(max_length=128, blank=True, null=True)
    user = models.ForeignKey(User)
    date = models.DateField(blank=True, null=True, default=timezone.now())


class PurchaseRequest(models.Model):
    pr_no = models.CharField(max_length=16)
    pr_creator = models.ForeignKey(User)
    pr_requisitioner = models.ForeignKey(Staff, related_name='requisitioner')
    pr_program = models.ForeignKey(Program, related_name='program')
    pr_department = models.ForeignKey(Department, related_name='department')
    pr_office = models.ForeignKey(Office, related_name='office')
    pr_date_prepared = models.DateField(blank=True, null=True, default=timezone.now())
    pr_date_needed = models.DateField()
    pr_justification = models.CharField(max_length=512)
    sig1 = models.ForeignKey(
        JSignatureModel,
        related_name='requested',
        blank=True,
        null=True
    )
    sig2 = models.ForeignKey(
        JSignatureModel,
        related_name='need_confirmed',
        blank=True,
        null=True
    )
    sig3 = models.ForeignKey(
        JSignatureModel,
        related_name='funds_available',
        blank=True,
        null=True
    )
    sig4 = models.ForeignKey(
        JSignatureModel,
        related_name='final_approval',
        blank=True,
        null=True
    )
    status = models.ForeignKey(
        'PRStatus',
        related_name='pr_status',
        default=1
    )

    def get_year(self):
        return self.pr_date_needed.year

    def get_value(self):
        items = PurchaseItem.objects.filter(pr=self)
        value = 0
        for item in items:
            try:
                value += item.totalprice
            except:
                pass
        return '$' + str(value)

    def is_overdue(self):
        return False  # logic needs writing

    def save(self, *args, **kwargs):
        # set PR status
        if not self.sig1:
            self.status = PRStatus.objects.get(id=1)
        if self.sig1:
            self.status = PRStatus.objects.get(id=2)
        if self.sig2:
            self.status = PRStatus.objects.get(id=3)
        if self.sig3:
            self.status = PRStatus.objects.get(id=4)
        if self.sig4:
            self.status = PRStatus.objects.get(id=5)

        # set PR number
        office = str(self.pr_office.name)
        year = str(self.get_year())[2:]
        queryset = PurchaseRequest.objects.filter(
            pr_office=self.pr_office)
        count = 1
        for obj in queryset:
            if obj.get_year == self.get_year:
                count += 1

        count = '{:04d}'.format(count)

        self.pr_no = office + " " + year + "-" + str(count)

        super(PurchaseRequest, self).save(*args, **kwargs)

    class Meta:
        permissions = (
            ("can_confirm_need", "Can confirm need"),
            ('can_confirm_funds_available', 'Can confirm funds available'),
            ('can_approve_low_value', 'Can approve low value PRs'),
            ('can_approve_high_value', 'Can approve high value PRs'),
        )


class PurchaseItem(models.Model):
    pr = models.ForeignKey(PurchaseRequest, blank=True, null=True)
    description = models.CharField(max_length=128)
    asset_class = models.CharField(max_length=16, blank=True, null=True)
    wbs = models.CharField(max_length=16, blank=True, null=True)
    qty = models.IntegerField()
    uom = models.CharField(max_length=12)
    price = models.DecimalField(max_digits=9, decimal_places = 2)
    totalprice = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places = 2)

    def save(self, *args, **kwargs):
        self.totalprice = decimal.Decimal(self.qty) * decimal.Decimal(self.price)
        super(PurchaseItem, self).save(*args, **kwargs)


class WBS(models.Model):
    pass



