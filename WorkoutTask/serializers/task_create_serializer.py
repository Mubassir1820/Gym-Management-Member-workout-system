# workouts/serializers/workout_task_create_serializer.py
from rest_framework import serializers
from WorkoutTask.models.workouttask import WorkoutTask
from users.models import User

class WorkoutTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutTask
        fields = [
            'id',
            'workout_plan',
            'member',
            'due_date',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        request = self.context['request']
        trainer = request.user
        member = data['member']
        workout_plan = data['workout_plan']

        if member.role != "member":
            raise serializers.ValidationError("Task can only be assigned to a member.")

        if member.gym_branch != trainer.gym_branch:
            raise serializers.ValidationError("Member must belong to your gym branch.")

        if workout_plan.gym_branch != trainer.gym_branch:
            raise serializers.ValidationError("Workout plan must belong to your branch.")

        if workout_plan.created_by != trainer:
            raise serializers.ValidationError("You can only assign tasks from your own workout plans.")

        return data
