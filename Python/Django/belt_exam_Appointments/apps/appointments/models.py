
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
import re
import bcrypt
email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
    def register_validator(self, data):
        errors = []
        if len(data['name']) < 2 or any(char.isdigit() for char in data['name']) :
            errors.append("Invalid First Name")   
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        if not email_regex.match(data['email']):
            errors.append("Invalid Email")       
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        elif data['password'] != data['confirmation'] :
            errors.append("password and confirmation aren't the same")
        if len(data['birth_day']) < 1:
            errors.append("please enter birthday")
        if self.filter(email=data['email']).count() > 0:
            errors.append("Someone with that email is already registered")  
        return errors
    def login_validator(self, data):
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
        #     errors.append("You haven't registered with that email yet")  
        return errors
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birth_day = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Appointments(models.Model):
    appointment_date = models.DateField(null=True, blank=True)
    time = models.TimeField(auto_now=False, null=True, blank=True)
    task = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name= "user_tasks")
    objects = UserManager()



