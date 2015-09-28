# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from custom_auth.forms import SignInForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            try:
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
            except IntegrityError:
                error_msg = 'این نام کاربری قبلا در سیستم ثبت شده است'
                return render(request, 'custom_auth/sign_in.html',
                              {'form': form, 'error_msg': error_msg})
                pass

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
