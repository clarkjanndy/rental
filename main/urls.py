from django.contrib import admin
from django.urls import path, include

from main.views import RentalListCreate, RentalRetrieveUpdateDestroy, ReservationListCreate, ReservationRetrieveUpdateDestroy

urlpatterns = [       
    path('rentals', RentalListCreate.as_view()),  
    path('rentals/<int:id>', RentalRetrieveUpdateDestroy.as_view()),    
    
    path('reservations', ReservationListCreate.as_view()),   
    path('reservations/<int:id>', ReservationRetrieveUpdateDestroy.as_view()), 
]
