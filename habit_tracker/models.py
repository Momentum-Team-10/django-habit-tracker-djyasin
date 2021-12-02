from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Habit(models.Model):
    habit = models.CharField(max_length=75, null=True)
    goal = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f"<Habit={self.habit}>"

    def __str__(self):
        return self.habit


class Record(models.Model):
    goal_progress = models.IntegerField(null=True)
    date_entered = models.DateTimeField(default=timezone.now, null=True)
    habit_id = models.ForeignKey('Habit', on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f"<DailyRecord habit={self.habit_id}"

    def __str__(self):
        return self.habit_id

