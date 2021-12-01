from django import forms
from .models import Habit, Record, User
from django.contrib.auth.forms import UserCreationForm


class HabitForm(forms.Form):
    class Meta:
        model = Habit
        fields = ["habit", "goal","created_at", "user_id"]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["goal_progress", "date_entered", "habit_id"]

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=100, help_text='Name')
    email = forms.EmailField(max_length=100, help_text='Email Address')

    class Meta:
        model = User
        fields =  ["username", "password", "email"]
