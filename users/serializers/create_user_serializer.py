from rest_framework import serializers
from users.models.users import User


class ManagerCreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role','gym_branch']
        read_only_fields = ['id']

    def validate_role(self, value):
        if value not in ['trainer', 'member']:
            raise serializers.ValidationError(
                "Manager can only create Trainer or Member."
            )
        return value

    def create(self, validated_data):
        request = self.context['request']
        manager = request.user

        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role'],
            gym_branch=manager.gym_branch
        )
        return user
