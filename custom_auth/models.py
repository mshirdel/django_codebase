# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    USER_GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=1, choices=USER_GENDER, default='M')
    marital_status = models.BooleanField(default=False)
    birth_day = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class UserPhone(models.Model):
    PHONE_TYPE = (
        ('C', 'Cell Phone'),
        ('H', 'Home'),
        ('W', 'Work Phone'),
        ('WF', 'Work Fax'),
        ('HF', 'Home Fax'),
        ('M', 'Main')
    )
    user = models.ForeignKey(UserProfile)
    phone_number = models.CharField(max_length=15)
    phone_type = models.CharField(max_length=2, choices=PHONE_TYPE)

    def __str__(self):
        return "%s %s %s" % (self.user.first_name + ' ', self.user.last_name, self.phone_number)


class ContactUs(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    name = models.CharField(max_length=200, blank=True, verbose_name='نام')
    comment = models.TextField(verbose_name='متن پیام')
    ip = models.GenericIPAddressField()
