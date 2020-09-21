from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CardSerializer
from core.serializers import UserSerializer
from .models import Card
from random import randint

def get_card_data(salary):
    score = randint(1,999)
    if(score >= 1 and score < 300):
        return { "status": False, "score": score,"limit": 0 }
    elif(score >= 300 and score < 600):
        return { "status": True, "score": score,"limit": 1000 }
    elif(score >= 600 and score < 800):
        limit = salary/2 if salary/2 > 1000 else 1000
        return { "status": True, "score": score,"limit": limit }
    elif(score >= 800 and score < 950):
        return { "status": True, "score": score,"limit": 2*salary }
    elif(score >= 951 and score < 1000):
        return { "status": True, "score": score,"limit": 1000000 }
    else:
        return { "status": False, "score": score,"limit": 0 }

@api_view(['POST'])
def create_card(request):
    """
    Creates a new card
    """
    try:
        user_salary = UserSerializer(request.user).data["salary"]
        card = Card.objects.create(**get_card_data(user_salary),user=request.user)
        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_card_id(request, card_id):
    """
    Updates card data based on given card_id (admin only)
    """
    try:
        card = Card.objects.filter(id=card_id)
        if not card:
            return Response({'error': 'Card does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CardSerializer(card[0], data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def find_card_id(request, card_id):
    """
    Returns card data based on given card_id (user must be the creator)
    """
    try:
        card = Card.objects.filter(user=request.user, id=card_id)
        if not card:
            return Response({'error': 'Card does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CardSerializer(card[0])
            return Response(serializer.data)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def findall_card(request):
    """
    Returns all cards (admin only)
    """
    try:
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
    except Exception:
        return Response({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_card_id(request, card_id):
    """
    Delete a card based on given card_id (user must be the creator)
    """
    try:
        card = Card.objects.get(user=request.user, id=card_id)
        card.delete()
        return Response({'message': 'Card removed succesfully'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'Deletion failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def find_card_user(request):
    """
    Returns all cards created by the user
    """
    try:
        cards = Card.objects.filter(user=request.user)
        if not cards:
            return Response([], status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CardSerializer(cards, many=True)
            return Response(serializer.data)
    except Exception:
        return Response({'error': 'Deletion failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def find_card_user_id(request, user_id):
    """
    Returns all cards created by the user with the given user_id
    """
    try:
        cards = Card.objects.filter(user=user_id)
        if not cards:
            return Response({'error': 'Card does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CardSerializer(cards, many=True)
            return Response(serializer.data)
    except Exception:
        return Response({'error': 'Deletion failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
