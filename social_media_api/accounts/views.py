from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
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
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_following(request):
    following = request.user.following.all()
    serializer = UserSerializer(following, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_followers(request):
    followers = request.user.followers.all()
    serializer = UserSerializer(followers, many=True)
    return Response(serializer.data)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        user_to_follow = get_object_or_404(User, id=user_id)

        if current_user == user_to_follow:
            return Response({'detail': 'You cannot follow yourself.'},
                status=status.HTTP_400_BAD_REQUEST)

        if user_to_follow in current_user.following.all():
            return Response({'detail': 'You are already following this user.'},
                status=status.HTTP_400_BAD_REQUEST)

        current_user.following.add(user_to_follow)
        return Response({'detail': 'User followed successfully.'},
            status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        user_to_unfollow = get_object_or_404(User, id=user_id)

        if current_user == user_to_unfollow:
            return Response({'detail': 'You cannot unfollow yourself.'},
                status=status.HTTP_400_BAD_REQUEST)

        if user_to_unfollow not in current_user.following.all():
            return Response({'detail': 'You are not following this user.'},
                status=status.HTTP_400_BAD_REQUEST)

        current_user.following.remove(user_to_unfollow)
        return Response({'detail': 'User unfollowed successfully.'},
            status=status.HTTP_200_OK)