from django.contrib.auth.models import User
from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    total_seats = models.IntegerField(default=60)
    available_seats = models.IntegerField(default=60)

    def __str__(self):
        return f'{self.flight_number} - {self.departure_date} {self.departure_time}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.flight.flight_number}'
