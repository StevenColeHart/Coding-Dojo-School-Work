# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import *

from django.shortcuts import render

def index(request):
    return render(request,'myrides/index.html')

def register(request):
    user = 
    request.session['current_user'] = User.objects.filter(username=request.POST['username'])[0].id

    return render(request, 'myrides/mainpage.html')

def mainpage(request):
    context = {
        user : User.objects.get(request, id=request.session)

    }



