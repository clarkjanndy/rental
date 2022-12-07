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
    
    def __str__(self):
        return "{} {} - {}".format(self.rental,self.check_in, self.check_out)