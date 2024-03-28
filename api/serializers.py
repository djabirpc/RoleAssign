from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Role, UserProfile

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    # Add custom claims
    token['role'] = UserProfile.objects.get(user = user).role.name
    # ...

    return token

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','username','password']
    extra_kwargs = {"password":{"write_only": True}}

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user

class AssignRoleSerializer(serializers.Serializer):
    username = serializers.CharField()
    role_name = serializers.CharField()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role']