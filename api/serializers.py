from rest_framework import serializers
from habit_tracker.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'pk',
            'habit',
            'goal',
            'created_at',
        )