from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    """
    Returns current user data based on their token
    """
    try:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    """
    Creates a new user (no token necessary)
    """
    try:
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'User successfully created', 'token': serializer.data["token"] }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_user(request):
    """
    Updates current user information based on their token
    """
    try:
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_user_id(request, user_id):
    """
    Updates user information based on given id (admin only)
    """
    try:
        user = get_user_model().objects.filter(id=user_id)
        if not user:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(user[0], data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def find_user_id(request, user_id):
    """
    Returns user data based on given id (admin only)
    """
    try:
        user = get_user_model().objects.filter(id=user_id)
        if not user:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(user[0])
            return Response(serializer.data)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def findall_user(request):
    """
    Returns all users (admin only)
    """
    try:
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)