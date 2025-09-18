from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),

    # Bookings app (home, services, booking form, etc.)
    path('', include('bookings.urls')),

    # User accounts app (register/profile)
    path('accounts/', include('useraccounts.urls')),       # custom user accounts
    path('accounts/', include('django.contrib.auth.urls')),  # built-in login/logout/password

    # Language switch endpoint
    path('i18n/setlang/', set_language, name='set_language'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)