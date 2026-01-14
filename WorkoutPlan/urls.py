# workouts/urls.py
from django.urls import path
from WorkoutPlan.views.workoutplan_view import WorkoutPlanListCreateView

urlpatterns = [
    path(
        'workout-plans/',
        WorkoutPlanListCreateView.as_view(),
        name='workout-plan-list-create'
    ),
]
