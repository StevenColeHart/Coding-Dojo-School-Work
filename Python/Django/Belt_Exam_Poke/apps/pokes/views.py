from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from .models import *


def index(request) :
   
    return render(request, 'pokes/index.html')

def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        password = bcrypt.hashpw("request.post['password']".encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], alias= request.POST['alias'], email=request.POST['email'], password=password)
        user.save()
        request.session['current_user'] = User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/success')

def login(request) :
    errors = User.objects.login_validator(request.POST)
    print request.POST
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    email= User.objects.get(email=request.['email'])
    if email == []:
        messages.error(request, "Invaild Email")
        return redirect('/')
    elif bcrypt.hashpw("request.post['password']".encode(), email.password.encode()):
        request.session['current_user'] =  email.id
        return redirect('/success')
    else:
        messages.error(request, "Invaild Email")
        return redirect('/')

def success(request):
    if "current_user" not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=request.session['current_user']),
        'users' : User.objects.all().exclude(id=request.session['current_user'])
    }
    return render(request,'pokes/success.html', context)

def logout(request):
    del request.session["current_user"]
    return redirect('/')

def poke(request, id):
    poker = User.objects.filter(id= request.session["current_user"])
    pokee = User.objects.get(id=id)
    Pokes.objects.create(poker=poker, pokee=pokee)
    return redirect("/success")

