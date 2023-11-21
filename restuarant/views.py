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
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Reservation submitted successfully'})
        else:
                print(form.errors)
    else: 
        form = BookingForm()
        context = {'form': form}
        return render(request, 'index.html', context)
    
    

def Reservation(request):
    reservations = Booking.objects.all()
    serializer = BookingSerializer(reservations, many=True)
    json_data = serializer.data
    return render(request, 'reservations.html', {'json_data': json_data})