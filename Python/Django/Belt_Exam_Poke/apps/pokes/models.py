# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
    def register_validator(self, data):
        errors = []
        if len(data['name']) < 2 or any(char.isdigit() for char in data['name']) :
            errors.append("Invalid Name")
        if len(data['alias']) < 2:
            errors.append("Invalid Alias, must be at least 2 characters")    
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        if not email_regex.match(data['email']):
            errors.append("Invalid Email")       
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        if data['password'] != data['confirmation'] :
            errors.append("password and confirmation aren't the same")
        if self.filter(email=data['email']).count() > 0:
            errors.append("Someone with that email is already registered")  
        return errors
    def login_validator(self, data):
        errors = []           
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        if not email_regex.match(data['email']):
            errors.append("Invalid Email")      
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        if self.filter(email=data['email']).count() < 1:
            errors.append("You haven't registered with that email yet")  
        # if not bcrypt.checkpw(data['password'].encode(), self.filter(email=data['email'])[0].password.encode()):
        #     errors.append("You haven't registered with that email yet")  
        return errors
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Pokes(models.Model):
    pokee = models.ForeignKey(User, related_name="got_poked")
    poker = models.ForeignKey(User, related_name="whos_poking")
    

