from django import forms
from .models import Booking, Service

class BookingForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        empty_label="-- Select a Service --",
        required=True
    )

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'service', 'vehicle_model', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
