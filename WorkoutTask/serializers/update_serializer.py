# workouts/serializers/workout_task_serializer.py
from rest_framework import serializers
from WorkoutTask.models.workouttask import WorkoutTask

class WorkoutTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutTask
        fields = [
            'id',
            'workout_plan',
            'status',
            'due_date',
            'created_at'
        ]
        read_only_fields = [
            'id',
            'workout_plan',
            'due_date',
            'created_at'
        ]
