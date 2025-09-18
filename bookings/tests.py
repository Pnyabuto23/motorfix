import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'motorfix.settings')
django.setup()

from django.test import TestCase
from .models import Service

class ServiceModelTest(TestCase):
    def test_create_service(self):
        service = Service.objects.create(
            name="Oil Change",
            description="Basic oil change service",
            price=50.00
        )
        self.assertEqual(str(service), "Oil Change")
