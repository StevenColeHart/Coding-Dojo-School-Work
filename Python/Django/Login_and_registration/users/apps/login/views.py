# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from models import *

# Create your views here.
def index(request) :

    return render(request, 'index.html')
   
def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        password = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password)
        user.save()
        request.session['current_user'] = User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/success')

def login(request) :
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['current_user'] =  User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/success')

def success(request):
    context = {
        'user' : User.objects.filter(id=request.session['current_user'])
    }
    return render(request, 'success.html', context)

