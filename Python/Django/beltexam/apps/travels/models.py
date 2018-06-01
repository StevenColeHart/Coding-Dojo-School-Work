# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, data):
        errors = []
        if len(data['name']) < 3 or any(char.isdigit() for char in data['name']) :
            errors.append("Invalid Name")
        if len(data['username']) < 3 or any(char.isdigit() for char in data['username']) :
            errors.append("Invalid Username")        
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        elif data['password'] != data['confirmation'] :
            errors.append("password and confirmation aren't the same")
        return errors
    def login_validator(self, data):
        errors = []           
        if len(data['email']) < 0:
            errors.append("Invalid Email")       
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        if self.filter(email=data['email']).count() < 1:
            errors.append("You haven't registered with that email yet")  
        elif bcrypt.checkpw(data['password'].encode(), self.filter(email=data['email'])[0].password.encode()):
            errors.append("You haven't registered with that email yet")  
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trips(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.


