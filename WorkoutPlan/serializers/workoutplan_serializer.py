# workouts/serializers/workout_plan_serializer.py
from rest_framework import serializers
from WorkoutPlan.models.workoutplan import WorkoutPlan

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = [
            'id',
            'title',
            'description',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']
