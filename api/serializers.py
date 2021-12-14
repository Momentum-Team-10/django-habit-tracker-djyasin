from rest_framework import serializers
from habit_tracker.models import Habit, Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = (
            'goal_progress',
            'date_entered',
        )
class RecordForHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('pk','habit', 'goal_progress', 'date_entered',)

class HabitSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True, read_only=True)
    class Meta:
        model = Habit
        fields = (
            'pk',
            'habit',
            'goal',
            'created_at',
            'records',
        )
