from django.contrib import admin
from .models import Habit, Record
from django.contrib.auth.admin import UserAdmin, User


admin.site.register(Habit)
admin.site.register(Record)
admin.site.register(User, UserAdmin)
# Register your models here.
