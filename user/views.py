from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
