# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from .models import *

# Create your views here.
def index(request) :
   
    return render(request, 'login/index.html')
   
def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        # if the errors {} has a length the for loop will go through all those errors and the display the messages.
        for error in errors:
            messages.error(request, error)
            # ^^^messages take in a ^request, post what the ^error is.
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password)
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

        # you can say print request.seesion ['current_user'] will print the id since it is equal to the above.^^^
        # your calling your request.session cureent user, this is you first DECLARING IT.
        # current user is the 
        # email=request.post because the login page only requires the email and password not a first name.
        # [0] is the index , grab the zero index grab the first thing [0] first which is the one that just logged and then put the id of that user 
        # into the request.session.
        print "I user did this"
        # do this to make sure pulling the correct information.
        print User.objects.filter(email=request.POST['email'])[0].first_name
        # filtering all the user objects that match the email being passed in by POST.
        # pulling all the users objects and is filter through them by what your trying to 
        # find which this result is the first_name because there is only one first name aka index [0]
        print User.objects.all()
        return redirect('/success')

def success(request):
    if "current_user" not in request.session:
        return redirect('/')
    joined=User.objects.get(id=request.session['current_user'])
    context = {
        'user' : User.objects.get(id=request.session['current_user']),
        'courses': Course.objects.all().exclude(students=joined.id),
        
        # *******************
        # were giving the name courses the value of the course model database so you can pass it to the template so that the html can use.
        # ***********
    }
    return render(request, 'login/success.html', context)

def add(request):
    return render(request, 'login/add.html')

def logout(request):
    del request.session["current_user"]
    return redirect('/')

def course(request,id):
    current_course = Course.objects.get(id=id)
    context = {
        "course":Course.objects.get(id=id),
        "enrolled_students":User.objects.all().filter(courses=current_course)
    }
    return render(request, "login/course.html", context)

def new(request):
    if request.method== 'POST':
        errors = Course.objects.Course_validator(request.POST)
        if len(errors):
            for error in errors:
                # this ^lets you put in multiple errors
                messages.error(request, error)
                # passing in the errors to your messages which will flash the errors.
            return redirect('/success')
        name_inputed=request.POST['course_name']
        description_inputed=request.POST['course_description']
        # THE PERSON WHO CREATED THIS COURSE
        creator=User.objects.get(id=request.session['current_user'])
        # ********
        # putting current user whs logged in id into the creator section of the database ********
        Course.objects.create(name=name_inputed,description=description_inputed,course_creator=creator)
        # the blue name is the name in course models*******
    return redirect('/success')

def join (request, id):
    name = User.objects.get(id=request.session["current_user"])
    course = Course.objects.get(id=id)
    # ^^above .courses is the courses in quotes in students in the Course models
    # pulling the user and course models t
    name.courses.add(course)
    return redirect("/success")

def drop(request,id):
    name=User.objects.get(id=request.session["current_user"])
    course = Course.objects.get(id=id)
    name.courses.remove(course)
    return redirect("/success")