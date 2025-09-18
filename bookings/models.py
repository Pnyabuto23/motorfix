from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    vehicle_model = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.vehicle_model} ({self.service.name})"
