from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Flight, Booking
from .forms import FlightForm, BookingForm, UserSignupForm

# User Views
def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'booking/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('search_flights')
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

@login_required
def search_flights_view(request):
    flights = Flight.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        flights = flights.filter(departure_date=date, departure_time=time)
    return render(request, 'booking/search_flights.html', {'flights': flights})

@login_required
def book_flight_view(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.flight = flight
            if flight.available_seats >= booking.seats_booked:
                flight.available_seats -= booking.seats_booked
                flight.save()
                booking.save()
                return redirect('my_bookings')
            else:
                form.add_error(None, "Not enough seats available.")
    else:
        form = BookingForm()
    return render(request, 'booking/book_flight.html', {'flight': flight, 'form': form})

@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# Admin Views
@login_required
def add_flight_view(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = FlightForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view_all_bookings')
        else:
            form = FlightForm()
        return render(request, 'booking/add_flight.html', {'form': form})
    else:
        return redirect('login')

@login_required
def remove_flight_view(request, flight_id):
    if request.user.is_staff:
        flight = get_object_or_404(Flight, id=flight_id)
        flight.delete()
        return redirect('view_all_bookings')
    else:
        return redirect('login')

@login_required
def view_all_bookings_view(request):
    if request.user.is_staff:
        bookings = Booking.objects.all()
        return render(request, 'booking/view_all_bookings.html', {'bookings': bookings})
    else:
        return redirect('login')
