from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Record
from .forms import HabitForm, RecordForm, UserForm
from django.contrib.auth.decorators import login_required

def home(request):
    user = request.user
    habits = Habit.objects.filter()

    return render(request, "home.html", {"habits": habits,})

def habit_library(request):
    user = request.user
    habits = Habit.objects.filter()
    return render(request, "habit_library.html", {"habits": habits,})

def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='/')

    return render(request, "habit_detail.html", {
        "form": form, "habit": habit, "pk": pk})

@login_required
def add_habit(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user
            form.save()
            return redirect(to='home')
    return render(request, "add_habit.html", {"form": form}) 
@login_required

def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='/')
    return render(request, "delete_habit.html",
                {"habit": habit})

@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='/')

    return render(request, "edit_habit.html", {
        "form": form, "habit": habit, "pk": pk})

@login_required
def add_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = RecordForm(instance=habit)
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.habit_id = habit
            form.save()
            return redirect('home')
    return render(request, 'add_record.html', {
        "form": form, "habit": habit})

