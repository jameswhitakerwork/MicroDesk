from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.utils import timezone
import datetime


# Create your models here.


class Simple_Model(models.Model):
    """
    Models where just a simple name is required
    can inherit from this model
    """
    name = models.CharField(max_length=32, unique=True)


    def __unicode__(self):
        return self.name


class Shirt_Size(Simple_Model):
    pass


class Staff_Type(Simple_Model):
    pass


class Warden_Zone(Simple_Model):
    pass


class Action(Simple_Model):
    pass


class Grade(Simple_Model):
    pass


class Contract_Type(Simple_Model):
    pass


class Position_Status(Simple_Model):
    class Meta:
        verbose_name_plural = 'Position Statuses'


class Duty_Station(Simple_Model):
    pass


class Program(Simple_Model):
    pass


class Gender(Simple_Model):
    pass


class Staff(models.Model):
    """
    Contains information about a particular person.
    Optionally matches up to a website user.
    Contains email, address, contact details.
    """

    user = models.OneToOneField(User, blank=True, null=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    staff_id = models.CharField(max_length=16)
    personnel_no = models.CharField(max_length=16)
    entry_on_duty = models.DateField(blank=True)
    shirt_size = models.ForeignKey(Shirt_Size, blank=True, null=True)
    no_of_dependants = models.IntegerField()
    staff_type = models.ForeignKey(Staff_Type)
    file = models.FileField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    gender = models.ForeignKey(Gender)
    nationality = CountryField()
    personal_email = models.EmailField(blank=True, null=True)
    home_phone = models.IntegerField(blank=True, null=True)
    mobile_phone = models.IntegerField(blank=True, null=True)
    home_phone_at_station = models.IntegerField(blank=True, null=True)
    mobile_phone_at_station = models.IntegerField(blank=True, null=True)
    address_1 = models.CharField(max_length=64, blank=True, null=True)
    address_2 = models.CharField(max_length=64, blank=True, null=True)
    address_3 = models.CharField(max_length=64, blank=True, null=True)
    address_country = CountryField()
    zip_code = models.CharField(max_length=8, blank=True, null=True)
    duty_address_1 = models.CharField(max_length=64, blank=True, null=True)
    duty_address_2 = models.CharField(max_length=64, blank=True, null=True)
    duty_address_3 = models.CharField(max_length=64, blank=True, null=True)
    duty_address_country = CountryField()
    duty_zip_code = models.CharField(max_length=8, blank=True, null=True)
    un_warden_zone = models.ForeignKey(Warden_Zone, blank=True, null=True)

    class Meta:
        verbose_name_plural = '   Staff'
        unique_together = ('first_name', 'last_name')

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name.upper()

    def save(self, *args, **kwargs):
        # change name to Lower UPPER
        self.last_name = self.last_name.upper()
        n = self.first_name
        print 'name is ' + n
        n1 = n[0]
        n2 = n[1:]
        n1 = n1.upper()
        n2 = n2.lower()
        self.first_name = n1 + n2
        print 'name has been changed to ' + self.first_name
        super(Staff, self).save(*args, **kwargs)

    def active_contract(self):
        c = Contract.objects.get(staff=self)
        if c:
            t = timezone.now().date()
            return c.start_date <= t <= c.end_date
        else:
            return False

    def position(self):
        p = Position.objects.get(staff=self.id)
        if p:
            return p.title
        else:
            return None

    active_contract.boolean = True


class Position(models.Model):
    """
    Position details such as grade, WBS, status
    """
    position_code = models.CharField(max_length=16)
    duty_station = models.ForeignKey(Duty_Station)
    program = models.ForeignKey(Program)
    title = models.CharField(max_length=64, unique=True)
    staff = models.ForeignKey(Staff, blank=True)
    reports_to = models.ForeignKey('Position', blank=True, null=True)
    tor = models.CharField(max_length=1024)
    start_date = models.DateField()
    expected_need_until = models.DateField(blank=True, null=True)
    expected_monthly_rate = models.IntegerField()
    wbs = models.CharField(max_length=32)
    status = models.ForeignKey(Position_Status)

    class Meta:
        verbose_name_plural = '  Positions'

    def __unicode__(self):
        return self.title

    def active_contract(self):
        c = Contract.objects.get(position=self)
        if c:
            t = timezone.now().date()
            return c.start_date <= t <= c.end_date
        else:
            return False

    active_contract.boolean = True


class Contract(models.Model):
    """
    Contract details with dates, rates and details.
    Also includes checklist for onboarding.
    A contract is matched to a particular staff member
    and a particular position.
    """
    position = models.ForeignKey(Position)
    staff = models.ForeignKey(Staff)
    contract_code = models.CharField(max_length=16)
    contract_type = models.ForeignKey(Contract_Type)
    file = models.FileField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.ForeignKey(Grade)
    monthly_rate = models.IntegerField()
    total_cost = models.IntegerField()
    action_after_expiration = models.ForeignKey(Action)
    personal_history = models.BooleanField(default=False)
    medical_clearance = models.BooleanField(default=False)
    policy_and_conduct = models.BooleanField(default=False)
    iom_email = models.BooleanField(default=False)
    basic_field_security = models.BooleanField(default=False)
    advanced_field_security = models.BooleanField(default=False)
    travel_profile = models.BooleanField(default=False)
    proof_of_life = models.BooleanField(default=False)
    ses_initiated = models.BooleanField(default=False)
    duty_station_orientation = models.BooleanField(default=False)
    photo = models.BooleanField(default=False)
    iom_un_id = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = ' Contracts'

    def __unicode__(self):
        return "Contract " + self.contract_code
