# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import UserProfile


class ContactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=False,
                           widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    email = forms.EmailField(label='Email', error_messages={'required': 'Email !!!'},
                             widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    url = forms.URLField(initial='http://',
                         widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    comment = forms.CharField(label='Comment', max_length=1024,
                              widget=forms.Textarea(attrs={'class': 'input-block-level'}))
    # cmb = forms.ComboField(fields=[forms.CharField(max_length=20), forms.EmailField()])


class SignInForm(forms.Form):
    user_name = forms.CharField(label='نام کاربری', max_length=30,
                                widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput(attrs={'class': 'input-block-level'}))
    # captcha = CaptchaField(label='عبارت تصویر زیر را وارد کنید')


class SignUpForm(forms.Form):
    first_name = forms.CharField(label='نام', max_length=100, required=False,
                                 widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    last_name = forms.CharField(label='نام خانوادگی', max_length=100, required=False,
                                widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    user_name = forms.EmailField(label='نام کاربری (ایمیل)', max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    password1 = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput(attrs={'class': 'input-block-level'}))
    password2 = forms.CharField(label='تکرار کلمه عبور',
                                widget=forms.PasswordInput(attrs={'class': 'input-block-level'}))


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'address', 'gender', 'marital_status', 'birth_day']
