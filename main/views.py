from django.shortcuts import render

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from main.models import Rental, Reservation
from main.serializers import RentalSerializer, ReservationSerializer

from rest_framework.response import Response
from django.http import HttpResponse
from django.db.models import F
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
    
    def list(self, request):
        queryset = Reservation.objects.select_related('rental').annotate(rental_name=F('rental__name'))
        serializer = self.serializer_class(queryset, many=True)
        
        return Response(serializer.data)
                
class ReservationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    def get(self, request, id):
        queryset = Reservation.objects.select_related('rental').filter(id=id).annotate(rental_name=F('rental__name'))
        serializer = self.serializer_class(queryset, many=True)
        
        return Response(serializer.data[0])
