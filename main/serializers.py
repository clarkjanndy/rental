from rest_framework import serializers
from main.models import Rental, Reservation

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'
    
class ReservationSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Reservation
        fields = ('rental','id','check_in', 'check_out',)
    
    def validate(self, data):
        if data['check_in'] > data['check_out']:
             raise serializers.ValidationError({'date error':'Check-In date must be a date before Check-Out date.'})
        return data
    
    def to_representation(self, instance):
        data = super(ReservationSerializer, self).to_representation(instance)
        #format the serialized data here
        data['id'] = 'Res-{}'.format(instance.id)
        data['rental'] = instance.rental.name
        data['previous_reservation'] =  self.previous_reservation(instance)
        return data

    @classmethod
    def previous_reservation(self, reservation):
        '''
        method to get the previous reservation of a certain rental.
        '''
        previous = Reservation.objects.filter(rental_id=reservation.rental_id).exclude(id__gte=reservation.id).last()
        if previous:
            return 'Res-{}'.format(previous.id)
        else:
            return '-'