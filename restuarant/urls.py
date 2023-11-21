
# from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    # path('submit_reservation/', views.submit_reservation, name='submit_reservation'),
    path('reservations/', views.Reservation, name='Reservation'), 
    # path('bookings', views.bookings, name='bookings'), 

]
