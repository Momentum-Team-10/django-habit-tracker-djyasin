from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from habit_tracker.models import Habit, Record
from .serializers import HabitSerializer, RecordSerializer


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

class DeleteHabitView(RetrieveDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class EditHabitView(RetrieveUpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class RecordLibraryView(APIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
    def get(self, request, format=None):
        habits = Habit.objects.all()
        records = Record.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data) 