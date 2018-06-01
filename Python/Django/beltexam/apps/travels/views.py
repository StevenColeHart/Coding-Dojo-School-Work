# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from models import *

def index(request) :
    return render(request, 'mybooks/index.html')

def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        password = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], username=request.POST['username'], password=password)
        user.save()
        request.session['current_user'] = User.objects.filter(username=request.POST['username'])[0].id
        return redirect('/success')

def login(request) :
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        username = request.session['current_user']
        username =  User.objects.filter(email=request.POST['email'])[0].id
        
        return redirect('/success')

def success(request):
    if 'current_user' not in request.session:
        return redirect('/')
    context={
        "user": user.objects.get(id=request.session['current_user']),
    }
    return render(request, 'travels/success.html', context)

