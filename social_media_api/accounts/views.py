from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        user_to_follow = get_object_or_404(get_user_model(), id=user_id)

        if user_to_follow in current_user.following.all():
            return Response({'detail': 'You are already following this user.'},
                status=status.HTTP_400_BAD_REQUEST)

        current_user.following.add(user_to_follow)
        current_user.save()
        return Response({'detail': 'User followed successfully.'},
            status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        user_to_unfollow = get_object_or_404(get_user_model(), id=user_id)

        if user_to_unfollow not in current_user.following.all():
            return Response({'detail': 'You are not following this user.'},
                status=status.HTTP_400_BAD_REQUEST)

        current_user.following.remove(user_to_unfollow)
        current_user.save()
        return Response({'detail': 'User unfollowed successfully.'},
            status=status.HTTP_200_OK)