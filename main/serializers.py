from rest_framework import serializers
from main.models import Rental, Reservation

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'
    
class ReservationSerializer(serializers.ModelSerializer):
    rental_name = serializers.CharField()
    class Meta:
        model = Reservation
        fields = ('rental_name','id','check_in', 'check_out', 'previous_reservation')
    
    def validate(self, data):
        if data['check_in'] > data['check_out']:
             raise serializers.ValidationError({'date error':'Check-In date must be a date before Check-Out date.'})
        return data