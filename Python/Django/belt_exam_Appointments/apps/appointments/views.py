# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from .models import *

def index(request) :
   
    return render(request, 'appointments/index.html')
   
def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], email=request.POST['email'], password=password, birth_day=request.POST['birth_day'] )
        user.save()
        print user
        request.session['current_user'] = User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/success')


def login(request) :
    errors = User.objects.login_validator(request.POST)
    print request.POST
    # this shows your the entire post tht you submitted in your login page
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['current_user'] =  User.objects.filter(email=request.POST['email'])[0].id

        return redirect('/success')

def success(request):
    if "current_user" not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=request.session['current_user']),
    }
    return render(request, 'appointments/success.html', context)
def newappointment(request):
    appointment = Appointments.objects.create(
        appointment_date=request.POST["appointment_date"],
        time= request.POST["appointment_time"],
        tasks=request.POST["task"], 
        user_tasks =request.session["current_user"] 
        )
    appointment.save()
    print appointment
    return redirect ('/success')

def logout(request):
    del request.session["current_user"]
    return redirect('/')

