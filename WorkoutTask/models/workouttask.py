from django.db import models
from WorkoutPlan.models.workoutplan import WorkoutPlan
from users.models.users import User

class WorkoutTask(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workout_tasks'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.workout_plan.title} -> {self.member.email}"
