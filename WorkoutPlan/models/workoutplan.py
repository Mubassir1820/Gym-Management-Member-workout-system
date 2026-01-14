from django.db import models
from django.conf import settings
from GymBranch.models.gym_branch import GymBranch

class WorkoutPlan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workout_plans"
    )
    gym_branch = models.ForeignKey(
        GymBranch,
        on_delete=models.CASCADE,
        related_name="workout_plans"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title