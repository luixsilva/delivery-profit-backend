from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from user.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .services.email_service import send_reset_email

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

        response = Response({'message': 'Logout successful'}, status=200)

        response.delete_cookie(
            key="auth_token",
            path="/",
            samesite="None",   
        )

        return response
    
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "name": user.name,
            "email": user.email,
        })
    

class PasswordResetRequestView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")

        user = User.objects.filter(email=email).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_url = f"https://delivery-profit-frontend.vercel.app/new-password?uid={uid}&token={token}"

            send_reset_email(user, reset_url)

            return Response({
                "message": "Se o email existir, um link de recuperação foi enviado."
            })


class PasswordResetConfirmView(APIView):
    permission_classes = []

    def post(self, request):
        uid = request.data.get("uid")
        token = request.data.get("token")
        new_password = request.data.get("new_password")

        try:    
            user_id = urlsafe_base64_encode(uid).decode()
            user = User.objects.get(pk=user_id)
        except:
            return Response({
                "error": "Invalid Link"
            }, status=400)    
        
        if not default_token_generator.check_token(user, token):
            return Response({
                "error": "Invalid or expired token"
            }, status=400)
        
        user.set_password(new_password)
        user.save()

        return Response({
            "message": "Password updated successfuly"
        })