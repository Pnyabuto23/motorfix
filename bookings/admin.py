from django.contrib import admin
from .models import Service, Booking

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "vehicle_model", "service", "date")
    list_filter = ("service", "date")
    search_fields = ("name", "email", "phone", "vehicle_model")
