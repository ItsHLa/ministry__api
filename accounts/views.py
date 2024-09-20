from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import Group
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User
from .serializers import SignUpSerializer, LoginSerializer, LogoutSerializer



# Create your views here.
@api_view(['POST'])
def signup(request):
    data = request.data
    user_data = SignUpSerializer(data = data)
    if user_data.is_valid():
        data = user_data.save()
        return Response(data, status=HTTP_201_CREATED)
    return Response(user_data.errors , status=HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.check_user(email=data['email'] , password=data['password'])
        if data is None:
            return Response({'message': 'user dose not exists'}, status=HTTP_400_BAD_REQUEST)
        return Response(data, status=HTTP_200_OK)
        
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    data = request.data
    serializer = LogoutSerializer(data = data)
    if serializer.is_valid():
        refresh = RefreshToken(data['refresh'])
        refresh.blacklist()
        return Response({
            'message': 'Log out successfully',
        })
    return Response(serializer.errors)