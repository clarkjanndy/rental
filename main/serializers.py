from rest_framework import serializers
from main.models import Rental, Reservation

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'
    
class ReservationSerializer(serializers.ModelSerializer):
    rental_name = serializers.CharField(read_only=True)    
    class Meta:
        model = Reservation
        fields = ('rental', 'rental_name','id','check_in', 'check_out', 'previous_reservation')
        
        read_only_fields = ['rental_name', ]
        extra_kwargs = {
            'rental': {'write_only': True},
            'previous_reservation': {'read_only': True},
        }
    
    def validate(self, data):
        if data['check_in'] > data['check_out']:
             raise serializers.ValidationError({'date error':'Check-In date must be a date before Check-Out date.'})
        return data