# workouts/views/workout_plan_views.py
from rest_framework.generics import ListCreateAPIView
from WorkoutPlan.models.workoutplan import WorkoutPlan
from WorkoutPlan.serializers.workoutplan_serializer import WorkoutPlanSerializer
from users.permissions import IsTrainer, IsManagerOrTrainer

class WorkoutPlanListCreateView(ListCreateAPIView):
    serializer_class = WorkoutPlanSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsTrainer()]
        return [IsManagerOrTrainer()]

    def get_queryset(self):
        user = self.request.user

        if user.role == "superadmin":
            return WorkoutPlan.objects.all()

        if user.role == "trainer":
            return WorkoutPlan.objects.filter(created_by=user)

        if user.role == "manager":
            return WorkoutPlan.objects.filter(
                gym_branch=user.gym_branch
            )

        return WorkoutPlan.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(
            created_by=user,
            gym_branch=user.gym_branch
        )
