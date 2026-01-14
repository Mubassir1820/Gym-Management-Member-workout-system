from django.urls import path
from WorkoutTask.views.workout_task_views import (
    WorkoutTaskCreateView,
    TrainerWorkoutTaskListView,
    MemberWorkoutTaskView,
)

urlpatterns = [
    path('tasks/assign/', WorkoutTaskCreateView.as_view()),
    path('tasks/trainer/', TrainerWorkoutTaskListView.as_view()),
    path('tasks/member/<int:pk>/', MemberWorkoutTaskView.as_view()),
]
