from django.contrib import admin
import main

# Register your models here.
admin.site.register(main.models.Rental)
admin.site.register(main.models.Reservation)
