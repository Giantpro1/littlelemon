from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .models import Booking
from .form import BookingForm
from .serializers import BookingSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def submit_reservation(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to 'Reservation' after successful form submission
            return redirect('Reservation')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = BookingForm()

    # If the form is not valid or it's a GET request, render the form page
    context = {'form': form}
    return render(request, 'index.html', context)
    
    

def Reservation(request):
    reservations = Booking.objects.all()
    serializer = BookingSerializer(reservations, many=True)
    json_data = serializer.data
    return render(request, 'reservations.html', {'json_data': json_data})