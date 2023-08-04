from django.conf import settings
from django.contrib.auth import authenticate
from .models import User as UserModel

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserSerializer
from .serializers import LoginSerializer

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the login index.")

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully."})
        return Response(serializer.errors, status=400)

class LoginClass(APIView):
    def get(self, request):
        return Response({
            'error_messages': 'Provide username and password.',
            'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request=request, username=username, password=password)
            # user = authenticate(request, username=serializer.validated_data['username'], password=serializer._validated_data['password'])
           
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                    'access_tolen_expires': int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()),
                    'refresh_expires': int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds()),
                }
                return Response(data, status=status.HTTP_200_OK)

            return Response({
                'error_message': 'Email or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)        
