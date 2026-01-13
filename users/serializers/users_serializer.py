from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    username_field = 'email'

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        data['user'] = {
            'id': user.id,
            'email': user.email,
            'role': user.role,
            # 'gym_branch': user.gym_branch.id if user.gym_branch else None
        }
        return data
