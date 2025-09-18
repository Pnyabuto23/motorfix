from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Service

@receiver(post_migrate)
def create_default_services(sender, **kwargs):
    if sender.name == "bookings":
        default_services = [
            {"name": "Oil Change", "description": "Keep your engine running smoothly.", "price": 3000},
            {"name": "Brake Service", "description": "Ensure safe braking performance.", "price": 5000},
            {"name": "Engine Diagnostics", "description": "Full engine check with diagnostic tools.", "price": 7000},
            {"name": "General Maintenance", "description": "Comprehensive car check and service.", "price": 4000},
        ]
        for service in default_services:
            Service.objects.get_or_create(
                name=service["name"],
                defaults={"description": service["description"], "price": service["price"]}
            )
