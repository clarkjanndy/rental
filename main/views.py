from django.shortcuts import render

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from main.models import Rental, Reservation
from main.serializers import RentalSerializer, ReservationSerializer

# Create your views here.
class RentalListCreate(ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class RentalRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class ReservationListCreate(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
