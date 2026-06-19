from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user.serializers import UserSerializer
from django.conf import settings


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()


        token, _ = Token.objects.get_or_create(user=user)

        response = Response(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
            },
            status=201,
        )

        response.set_cookie(
            key="auth_token",
            value=token.key,
            httponly=True,
            secure=not settings.DEBUG, 
            samesite="Lax",
        )

        return response