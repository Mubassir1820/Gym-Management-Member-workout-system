from rest_framework.generics import CreateAPIView, ListAPIView
from users.serializers.create_user_serializer import ManagerCreateUserSerializer
from users.models.users import User
from users.permissions import IsManager

class ManagerCreateUserView(CreateAPIView):
    serializer_class = ManagerCreateUserSerializer
    permission_classes = [IsManager]

class ManagerUserListView(ListAPIView):
    serializer_class = ManagerCreateUserSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        manager = self.request.user
        return User.objects.filter(
            gym_branch=manager.gym_branch
        ).exclude(role='super_admin')
