from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from bookings.models import Booking   # ✅ import your Booking model


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "useraccounts/register.html", {"form": form})


@login_required
def profile(request):
    # ✅ Fetch user’s bookings by email
    bookings = Booking.objects.filter(email=request.user.email)

    return render(request, "useraccounts/profile.html", {
        "bookings": bookings
    })
