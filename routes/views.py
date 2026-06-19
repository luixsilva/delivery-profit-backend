from django.shortcuts import render
from rest_framework import generics
from routes.models import Route
from routes.serializers import RouteSerializer
from rest_framework.permissions import IsAuthenticated

class RouteCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Route.objects.all()
    serializer_class = RouteSerializer    