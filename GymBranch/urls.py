from django.urls import path
from GymBranch.views.gym_branch_views import GymBranchListCreateView

urlpatterns = [
    path('', GymBranchListCreateView.as_view(), name='branch-list-create'),
]
