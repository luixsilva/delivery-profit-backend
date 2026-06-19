from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user =   authenticate(
            email=email,
            password=password
              )
        

        if user:
            token, created = Token.objects.get_or_create(user=user)
            response = Response({
                'message': 'Login  successful',
            },
              status=200)
            
            
            response.set_cookie(
                key="auth_token",
                value=token.key,
                httponly=True,
                secure=True,
                samesite="None",
                max_age=3600,
            )
            
            return response
        else:
            return Response({
                'error': 'Invalid Credentials'},
                status=401
            )
        
class LogoutView(APIView): 
    permission_classes = [IsAuthenticated]

    def post(self, request):

        token = request.COOKIES.get("auth_token")

        if token:
            Token.objects.filter(key=token).delete()

        response = Response({
            'message': 'Logout successful',
        },
            status=200)

        response.delete_cookie('auth_token')

        return response  
    
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print('User', user)
        print("COOKIES:", request.COOKIES)
        print("USER:", request.user)
        print("AUTH:", request.auth)
        return Response({
            "id": user.id,
            "name": user.name,
            "email": user.email,
        })