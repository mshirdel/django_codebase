# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import UserProfile, ContactUs


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
    user_name = forms.EmailField(label='نام کاربری (ایمیل)',
                                 max_length=30,
                                 error_messages={
                                     'required': 'لطفا ایمیل خود را وارد کنید',
                                     'invalid': 'لطفا ایمیل معتبری وارد کنید'
                                 },
                                 widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    password1 = forms.CharField(label='کلمه عبور',
                                error_messages={'required': 'کلمه عبور دلخواه خود را وارد کنید'},
                                widget=forms.PasswordInput(attrs={'class': 'input-block-level'}))
    password2 = forms.CharField(label='تکرار کلمه عبور',
                                error_messages={'required': 'کلمه عبور دلخواه خود را وارد کنید'},
                                widget=forms.PasswordInput(attrs={'class': 'input-block-level'}))


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'address', 'gender', 'marital_status', 'birth_day']


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'name', 'comment']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'input-block-level'}),
            'name': forms.TextInput(attrs={'class': 'input-block-level'}),
            'comment': forms.Textarea(attrs={'class': 'input-block-level'})
        }
        error_messages = {
            'email': {
                'required': 'لطفا ایمیل معتبری وارد کنید'
            },
            'comment': {
                'required': 'متن پیام مورد نظر را وارد کنید'
            }
        }
