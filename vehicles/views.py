from django.shortcuts import render
from rest_framework import generics
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from rest_framework.permissions import IsAuthenticated

class VehiclesCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehiclesRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
