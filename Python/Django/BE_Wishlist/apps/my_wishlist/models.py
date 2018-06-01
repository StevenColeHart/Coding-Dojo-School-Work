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
        if len(data['name']) < 3 or any(char.isdigit() for char in data['name']) :
            errors.append("Invalid First Name")
        if len(data['user_name']) < 3 or any(char.isdigit() for char in data['user_name']) :
            errors.append("Invalid Username")    
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
        errors = []           
        if len(data['user_name']) < 0:
             errors.append("Invalid Username")     
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        if self.filter(user_name=data['user_name']).count() < 1:
            errors.append("You haven't registered yet")  
        elif bcrypt.checkpw(data['password'].encode(), self.filter(user_name=data['user_name'])[0].password.encode()):
            errors.append("You haven't registered yet")  
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class ItemManager(models.Manager):
    def item_validator(self, data):
        errors = []
        if len(data['item_name']) < 2:
            errors.append("Invalid Item Name")    
        return errors

class Items(models.Model):
    item_name = models.CharField(max_length=255)
    item_creator = models.ForeignKey(User,related_name='created_item')
    wish_listers = models.ManyToManyField(User,related_name='wishlist')
    created_at= models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    objects=ItemManager()