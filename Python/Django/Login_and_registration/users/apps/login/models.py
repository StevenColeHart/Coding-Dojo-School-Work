# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt


# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, data):
        errors = []
        if len(data['first_name']) < 2 or any(char.isdigit() for char in data['first_name']) :
            errors.append("Invalid First Name")
        if len(data['last_name']) < 2 or any(char.isdigit() for char in data['last_name']) :
            errors.append("Invalid Last Name")    
        if len(data['email']) < 0 or re.match(r"[^@]+@[^@]+\.[^@]+", data['email']) == None :
            errors.append("Invalid Email")       
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        elif data['password'] != data['confirmation'] :
            errors.append("password and confirmation aren't the same")
        if self.filter(email=data['email']).count() > 0:
            errors.append("Someone with that email is already registered")  
        return errors
    def login_validator(self, data):
        errors = []           
        if len(data['email']) < 0 or re.match(r"[^@]+@[^@]+\.[^@]+", data['email']) == None :
            errors.append("Invalid Email")       
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        if self.filter(email=data['email']).count() < 1:
            errors.append("You haven't registered with that email yet")  
        elif bcrypt.checkpw(data['password'].encode(), self.filter(email=data['email'])[0].password.encode()):
            errors.append("You haven't registered with that email yet")  
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
