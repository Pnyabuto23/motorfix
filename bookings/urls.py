from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('book/', views.booking_form, name='booking_form'),
    path('book/<int:service_id>/', views.booking_form, name='booking_with_service'),
    path('book/success/', views.booking_success, name='booking_success'),
    path('about/', views.about, name='about'),
]