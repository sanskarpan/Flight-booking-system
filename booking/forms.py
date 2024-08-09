from django import forms
from .models import Flight, Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seats_booked']
