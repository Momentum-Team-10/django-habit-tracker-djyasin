from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from habit_tracker.models import Habit
from .serializers import HabitSerializer


class HabitLibraryView(APIView):
    def get(self, request, format=None):
        habits = Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)

        return Response(serializer.data)

class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class CreateHabitView(CreateAPIView):
    serializer_class = HabitSerializer