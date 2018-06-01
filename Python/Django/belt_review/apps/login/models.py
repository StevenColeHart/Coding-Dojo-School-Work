# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# Create your models here.
class UserManager(models.Manager):
    # in classes when you are defining function they must have (self, and data 
    def register_validator(self, data):
        errors = []
        if len(data['first_name']) < 2 or any(char.isdigit() for char in data['first_name']) :
            errors.append("Invalid First Name")
        if len(data['last_name']) < 2 or any(char.isdigit() for char in data['last_name']) :
            errors.append("Invalid Last Name")    
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        if not email_regex.match(data['email']):
            errors.append("Invalid Email")       
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        elif data['password'] != data['confirmation'] :
            errors.append("password and confirmation aren't the same")
        if self.filter(email=data['email']).count() > 0:
            errors.append("Someone with that email is already registered")  
        return errors
    def login_validator(self, data):
        # these are the checks in the views.py def login for errors.
        errors = []           
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        elif not email_regex.match(data['email']):
            errors.append("Invalid Email")      
        elif len(data['password']) < 8 :
            errors.append("Password is too short")   
        elif self.filter(email=data['email']).count() < 1:
            errors.append("You haven't registered with that email yet")  
        # if bcrypt.checkpw(data['password'].encode(), self.filter(email=data['email'])[0].password.encode()):
            # errors.append("You haven't registered with that email yet")  
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()

class CourseManager(models.Manager):
    def Course_validator(self, data):
        # data ^^^is a dictionary and you are calling the values that are associated with your keys of that dictionary(of your inputs for the login).
    # all functions include themselves
    # when your creating the function it pulls in from self and the data
        errors = []
        if len(data['course_name']) < 2 or any(char.isdigit() for char in data['course_name']) :
            errors.append("Invalid Course Name")
        if len(data['course_description']) < 2 :
            #the name 'course_description' is being pulled from the form data on the html page, not from the field specified in the class on this here models page.
            errors.append("Invalid Description")      
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=500)
    # one to many relationship
    course_creator = models.ForeignKey(User,related_name='created_course')
    # its the course the creator made its a way to link them
    # this is a many to many field relationship
    students = models.ManyToManyField(User,related_name='courses')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # if you wanted to display the newest stuff first your going to want to filter through which is why we will ALWAYS have created_at and updated_at
    objects=CourseManager()
    # you put objects at the bottom because this is how you link
    # dont mforget parenthesis 

# class Book(models.Model):
#      title= models.CharField(max_length=255)
#      author=models.ForeignKey(Author, related_name='authorsbooks')
#      uploader = models.ForeignKey(User)
#     #  what exactly are we trying to do here?? This is like creators in puppies
#     # is this like current users??
#      created_at = models.DateTimeField(auto_now_add=True)
#      updated_at =models.DateTimeField(auto_now=True)


