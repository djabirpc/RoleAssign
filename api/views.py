from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import  Role, UserProfile
from .permissions import IsRole
from rest_framework import generics
from .serializers import UserSerializer, RoleSerializer,AssignRoleSerializer

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]

class HRPage(generics.GenericAPIView):
    required_roles = ["HR"]
    permission_classes = [IsAuthenticated, IsRole, IsAdminUser]

    def get(self, request):
        # Your HR specific logic here
        return Response("HR Page Content")

class CreateRole(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]

class AssignRoleToUser(generics.CreateAPIView):
    """
    API endpoint to assign roles to users.
    Only admin users can access this endpoint.
    """
    queryset = Role.objects.all()
    serializer_class = AssignRoleSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
      username = serializer.validated_data.get('username')
      role_name = serializer.validated_data.get('role_name')

      try:
          user = User.objects.get(username=username)
      except User.DoesNotExist:
          raise NotFound({"error": "User does not exist"})
      
      try:
        role= Role.objects.get(name = role_name)
      except Role.DoesNotExist:
          raise NotFound({"error": "Role does not exist"})

      user_profile = UserProfile.objects.create(user = user, role = role)
      user_profile.save()
      return Response(status = status.HTTP_201_CREATED)

