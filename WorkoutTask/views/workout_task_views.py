from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from WorkoutTask.models.workouttask import WorkoutTask
from WorkoutTask.serializers.task_create_serializer import WorkoutTaskCreateSerializer
from WorkoutTask.serializers.update_serializer import WorkoutTaskSerializer
from users.permissions import IsTrainer, IsMember

class WorkoutTaskCreateView(CreateAPIView):
    serializer_class = WorkoutTaskCreateSerializer
    permission_classes = [IsTrainer]

class TrainerWorkoutTaskListView(ListAPIView):
    serializer_class = WorkoutTaskSerializer
    permission_classes = [IsTrainer]

    def get_queryset(self):
        user = self.request.user
        return WorkoutTask.objects.filter(
            workout_plan__created_by=user
        ).select_related('workout_plan', 'member')

class MemberWorkoutTaskView(RetrieveUpdateAPIView):
    serializer_class = WorkoutTaskSerializer
    permission_classes = [IsMember]

    def get_queryset(self):
        return WorkoutTask.objects.filter(
            member=self.request.user
        )

    def perform_update(self, serializer):
        serializer.save()
