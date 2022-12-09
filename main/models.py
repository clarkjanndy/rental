from django.db import models

# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
        
    def rental_name(self):
        return self.rental.name
    
    def previous_reservation(self):
        previous = Reservation.objects.filter(rental_id=self.rental_id).exclude(id__gte=self.id).last()
        return previous.id if (previous) else ' - '
    
    def __str__(self):
        return "{} {} - {}".format(self.rental,self.check_in, self.check_out)