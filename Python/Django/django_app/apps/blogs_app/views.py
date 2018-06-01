# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response= "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    respone= "placeholder to display a new form"
    return HttpResponse(respone)

def create(request):
    return redirect('/')


# Create your views here.
