from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import BookingForm

def home(request):
    services = Service.objects.all()
    return render(request, 'bookings/home.html', {'services': services})

def services(request):
    services = Service.objects.all()
    return render(request, 'bookings/services.html', {'services': services})

def booking_form(request, service_id=None):
    service_instance = None
    if service_id:
        service_instance = get_object_or_404(Service, id=service_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        # Pre-fill the service if a service_id is passed
        form = BookingForm(initial={'service': service_instance}) if service_instance else BookingForm()

    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

def about(request):
    return render(request, 'bookings/about.html')
