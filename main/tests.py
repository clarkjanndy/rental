from django.urls import reverse
from rest_framework.test import APITestCase
from main.models import Rental, Reservation

# Create your tests here.
class Test(APITestCase):

    #set up test data here
    def setUp(self):
        rental1=Rental.objects.create(name='rental-1')
        rental2=Rental.objects.create(name='rental-2')

        Reservation.objects.create(rental=rental1, check_in='2022-01-01', check_out='2022-01-13')
        Reservation.objects.create(rental=rental1, check_in='2022-01-20', check_out='2022-02-10')
        Reservation.objects.create(rental=rental1, check_in='2022-02-20', check_out='2022-03-10')
        Reservation.objects.create(rental=rental2, check_in='2022-01-02', check_out='2022-01-20')
        Reservation.objects.create(rental=rental2, check_in='2022-01-11', check_out='2022-01-20')


    def test_1(self):
        response = self.client.get('/reservations/1', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['rental_name'], 'rental-1')
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['check_in'], '2022-01-01')
        self.assertEqual(response.data['check_out'], '2022-01-13')
        self.assertEqual(response.data['previous_reservation'], ' - ')
    
    def test_2(self):
        response = self.client.get('/reservations/2', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['rental_name'], 'rental-1')
        self.assertEqual(response.data['id'], 2)
        self.assertEqual(response.data['check_in'], '2022-01-20')
        self.assertEqual(response.data['check_out'], '2022-02-10')
        self.assertEqual(response.data['previous_reservation'], 1)
    
    def test_3(self):
        response = self.client.get('/reservations/3', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['rental_name'], 'rental-1')
        self.assertEqual(response.data['id'], 3)
        self.assertEqual(response.data['check_in'], '2022-02-20')
        self.assertEqual(response.data['check_out'], '2022-03-10')
        self.assertEqual(response.data['previous_reservation'], 2)
    
    def test_4(self):
        response = self.client.get('/reservations/4', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['rental_name'], 'rental-2')
        self.assertEqual(response.data['id'], 4)
        self.assertEqual(response.data['check_in'], '2022-01-02')
        self.assertEqual(response.data['check_out'], '2022-01-20')
        self.assertEqual(response.data['previous_reservation'], ' - ')
    
    def test_5(self):
        response = self.client.get('/reservations/5', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['rental_name'], 'rental-2')
        self.assertEqual(response.data['id'], 5)
        self.assertEqual(response.data['check_in'], '2022-01-11')
        self.assertEqual(response.data['check_out'], '2022-01-20')
        self.assertEqual(response.data['previous_reservation'], 4)

    
    
        
        
