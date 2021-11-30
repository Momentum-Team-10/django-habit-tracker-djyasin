from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    # def __repr__(self):
    #     # return f"<User username={self.username}>"
        

    def __str__(self):
        return self.username

class Habit(models.Model):
    habit = models.CharField(max_length=75)
    goal = models.CharField(max_length=75)
    # make this an integer field 
    # Add unit char, investigate that
    # habit created date
    # Add PK user relationship 
    # Must be logged in to use

class Record(models.Model):
    pass
    # frequency = models.BooleanField()
    # # do I want this?
    
