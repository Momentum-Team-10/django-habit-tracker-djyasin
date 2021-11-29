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
    frequency = models.BooleanField()
    
