from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Record
from .forms import HabitForm, RecordForm, UserForm
from django.contrib.auth.decorators import login_required

def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save()
            habit.save()
            return redirect("add_habit.html", habit_pk=habit.pk)
    else:
        form = HabitForm()
    return render(request, "add_habit.html", {"form": form}) 

