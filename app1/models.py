from django.db import models
import re
class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['fname'])<4:
            errors['fname']="First name should be a t least 4 characters!"
        if len(postData['lname'])<4:
            errors['lname']="Last name should be a t least 4 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email']="Invalid Email Address"
        if len(postData['password'])<8:
            errors['password']="Password should be a t least 8 characters!"
        if postData['password'] != postData['confirm']:
            errors['confirm']="Passwords don't match!"
        return errors
# Create your models here.
class User(models.Model):
    first = models.CharField(max_length=45)
    last= models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()


