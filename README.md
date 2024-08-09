# Flight Booking System

This is a Django-based web application for flight booking with separate user and admin interfaces. The application allows users to search for flights, book tickets, and view their bookings. Admins can manage flights and view bookings by flight number and time.

## Features

### User Types
1. **User**
2. **Admin**

### User Use Cases
- **Login:** Users can log in with their credentials.
- **Sign Up:** New users can create an account to access the platform.
- **Search for Flights:** Users can search for available flights based on date and time.
- **Book Tickets:** Users can book tickets on a selected flight based on availability (default seat count is 60).
- **My Bookings:** Users can view a list of all their bookings.
- **Logout:** Users can securely log out of the application.

### Admin Use Cases
- **Login:** Admins have a separate login interface.
- **Add Flights:** Admins can add new flights to the system.
- **Remove Flights:** Admins can remove existing flights from the system.
- **View Bookings:** Admins can view all bookings based on flight number and time.


## Installation

### Prerequisites

- Python 3.9+
- Django 4.0
- A PostgreSQL/MySQL database (or SQLite for development)
- Git (for cloning the repository)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Flight-booking-system.git
   cd Flight-booking-system
   ```
2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install the Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a Superuser (Admin Account)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
Visit `http://127.0.0.1:8000/` in your browser.

## Testing the Application
### User Interface
1. Sign Up and Log In:
- Create a user account and log in.
2. Search and Book Flights:
- Use the search functionality to find flights and book available seats.
3. View My Bookings:
- Check the "My Bookings" section to see all your bookings.
4. Logout:
- Log out from the user interface.
### Admin Interface
1. Log In:
- Log in using the admin credentials.
2. Manage Flights:
- Add new flights and remove existing ones.
3. View Bookings:
- View bookings filtered by flight number and time.

