from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from habit_tracker.models import Habit
from .serializers import HabitSerializer



class HabitLibraryView(APIView):
    def get(self, request, format=None):
        habits = Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)

        return Response(serializer.data)
