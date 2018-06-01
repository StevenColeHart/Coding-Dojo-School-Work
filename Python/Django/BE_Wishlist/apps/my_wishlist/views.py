# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from .models import User, Items

def index(request) :
   
    return render(request, 'my_wishlist/index.html')
   
def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        password = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], user_name=request.POST['user_name'], email=request.POST['email'], password=password)
        user.save()
        request.session['current_user'] = User.objects.filter(user_name=request.POST['user_name'])[0].id
        return redirect('/success')

def login(request) :
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['current_user'] =  User.objects.filter(user_name=request.POST['user_name'])[0].id
        return redirect('/success')

def success(request):
    if "current_user" not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=request.session['current_user']),
        'mywishlists': Items.objects.all().filter(wish_listers=)
    }
    return render(request, 'my_wishlist/success.html', context)

def logout(request):
    del request.session["current_user"]
    return redirect('/')

def add(request):
    return render(request, 'my_wishlist/add.html')

def new(request):
    if request.method== 'POST':
        errors = Items.objects.item_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
            return redirect('/add')
    else:
        name_inputed=request.POST['item_name']
        creator=User.objects.get(id=request.session['current_user'])
        Items.objects.create(item_name=name_inputed,item_creator=creator)
    return redirect('/add')



