from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views.users_views import LoginView,ProfileView
from users.views.create_users import ManagerCreateUserView, ManagerUserListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('manager/users/', ManagerCreateUserView.as_view(), name='manager-create-user'),
    path('manager/users/list/', ManagerUserListView.as_view(), name='manager-user-list')


]