from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

User = get_user_model()


class UserCreateView(CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserRetriveView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
