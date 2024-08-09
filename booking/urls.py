from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search_flights/', views.search_flights_view, name='search_flights'),
    path('book_flight/<int:flight_id>/', views.book_flight_view, name='book_flight'),
    path('my_bookings/', views.my_bookings_view, name='my_bookings'),
    path('admin/add_flight/', views.add_flight_view, name='add_flight'),
    path('admin/remove_flight/<int:flight_id>/', views.remove_flight_view, name='remove_flight'),
    path('admin/view_all_bookings/', views.view_all_bookings_view, name='view_all_bookings'),
]
