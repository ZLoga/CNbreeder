# coding=utf-8
from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from CNB_account.models import User
import datetime


def login(request):
    if request.method == "POST":
        uf = UserFormLogin(request.POST)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userresult = User.objects.filter(username=username, password=password)
            # pdb.set_trace()
            if len(userresult) > 0:
                return render_to_response('CNB_account/success.html',
                                          {'operation': "登录"},
                                          context_instance=RequestContext(request))
            else:
                return HttpResponse("该用户不存在")
    else:
        uf = UserFormLogin()
        return render_to_response("CNB_account/userlogin.html", {'uf': uf}, context_instance=RequestContext(request))


def register(request):
    now = datetime.datetime.now()
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            filterresult = User.objects.filter(username=username)
            if len(filterresult) > 0:
                return render_to_response('CNB_account/register.html',
                                          {'uf': uf,
                                           "errors": "用户名已存在"},
                                          context_instance=RequestContext(request))
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                if password2 != password1:
                    return render_to_response('CNB_account/register.html',
                                              {'uf': uf,
                                               'errors': "两次输入的密码不一致!"},
                                              context_instance=RequestContext(request))
                    # return HttpResponse('两次输入的密码不一致!,请重新输入密码')
                email = uf.cleaned_data['email']
                # 将表单写入数据库
                user = User.objects.create(username=username, password=password2)
                # user = User(username=username,password=password,email=email)
                user.save()
                # 返回注册成功页面
                return render_to_response('CNB_account/success.html',
                                          {'username': username, 'operation': "注册"},
                                          context_instance=RequestContext(request))
    else:
        uf = UserForm()
        return render_to_response('CNB_account/register.html', {'uf': uf}, context_instance=RequestContext(request))


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')


class UserFormLogin(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
