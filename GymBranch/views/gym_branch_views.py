from rest_framework.generics import ListCreateAPIView
from GymBranch.models.gym_branch import GymBranch
from GymBranch.serializers.gym_branch_serializer import GymBranchSerializer
from users.permissions import IsSuperAdmin

class GymBranchListCreateView(ListCreateAPIView):
    queryset = GymBranch.objects.all()
    serializer_class = GymBranchSerializer
    permission_classes = [IsSuperAdmin]