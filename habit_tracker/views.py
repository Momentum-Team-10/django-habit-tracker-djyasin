from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Record
from .forms import HabitForm, RecordForm, UserForm
from django.contrib.auth.decorators import login_required

def home(request):
    user = request.user
    habits = Habit.objects.filter(user=user.pk)

    return render(request, "habit_tracker/home.html", {
        "user": user, "habits": habits,})

# @login_required
def add_habit(request):
    user = request.user
    if request.method == "GET":
        form = HabitForm()
    else: 
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user_id = user.pk
            form.save()
            return redirect(to='home')
    return render(request, "add_habit.html", {"form": form, "user": user}) 

