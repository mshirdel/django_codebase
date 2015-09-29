# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from custom_auth.forms import SignInForm, SignUpForm, ContactUsForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from custom_auth.models import ContactUs
from my_utils import http

# Create your views here.


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            error_msg = 'نام کاربری یا کلمه عبور اشتباه است'
            user = authenticate(username=form.cleaned_data['user_name'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'custom_auth/user_activation_request.html')
            else:
                return render(request, 'custom_auth/sign_in.html',
                              {'form': form, 'error_msg': error_msg})
        else:
            error_msg = 'لطفا نام کاربری و کلمه عبور را وارد کنید'
            form = SignInForm()
            return render(request, 'custom_auth/sign_in.html',
                          {'form': form, 'error_msg': error_msg})
    else:
        form = SignInForm()
        return render(request, 'custom_auth/sign_in.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:

                pass2 = form.cleaned_data['password2']
                pass1 = form.cleaned_data['password1']
                user_name = form.cleaned_data['user_name']
                if pass1 == pass2:
                    new_user = User.objects.create_user(username=user_name, email=user_name,
                                                        password=pass1)
                    new_user.is_active = False
                    new_user.save()
                    return render(request, 'custom_auth/sign_up.html',
                                  {'form': form,
                                   'success_msg': 'حساب کاربری شما ایجاد شد. برای فعال سازی ایمیل خود را چک کنید'})
                else:
                    return render(request, 'custom_auth/sign_up.html',
                                  {'form': form,
                                   'error_msg': 'کلمه های عبور وارد شده با هم برابر نمی باشند'})
            except IntegrityError:
                return render(request, 'custom_auth/sign_up.html',
                              {'form': form,
                               'error_msg': 'این نام کاربری قبلا ثبت شده است'})

        else:
            return render(request, 'custom_auth/sign_up.html',
                          {'form': form,
                           'error_msg': 'فیلدهای الزامی را پر کنید'})
    else:
        form = SignUpForm()
    return render(request, 'custom_auth/sign_up.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def contact_us(request):
    if request.method == 'POST':
        contact = ContactUs(ip=http.get_client_ip(request))
        form = ContactUsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return render(request, 'custom_auth/contact_us.html',
                          {
                              'form': form,
                              'success_msg': 'پیام شما در سیستم ثیت شد'
                          })
        else:
            return render(request, 'custom_auth/contact_us.html',
                          {
                              'form': form,
                              'error_msg': 'لطفا فیلدهای الزامی را پر کنید'
                          })
    else:
        form = ContactUsForm
    return render(request, 'custom_auth/contact_us.html', {'form': form})
