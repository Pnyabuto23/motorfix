from pathlib import Path
import os
import dj_database_url
from django.utils.translation import gettext_lazy as _

# ---------------------------
# BASE DIRECTORY
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# SECURITY
# ---------------------------
# Secret key from environment, fallback for local dev
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'replace-this-with-a-secure-key')

# DEBUG from env (True/False). Works in Windows, Linux, Render.
DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 'yes']

# ---------------------------
# ALLOWED HOSTS
# ---------------------------
# Always allow localhost + 127.0.0.1 for dev
# Plus your Render domain by default
ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "motorfix.onrender.com,localhost,127.0.0.1"
).split(",")

# ---------------------------
# INSTALLED APPS
# ---------------------------
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'bookings',
    'useraccounts',

    # Third-party apps
    'crispy_forms',
    'widget_tweaks',
    'django_extensions',
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

# ---------------------------
# MIDDLEWARE
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------
# URLS & WSGI
# ---------------------------
ROOT_URLCONF = 'motorfix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates", BASE_DIR / "bookings" / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'motorfix.wsgi.application'
ASGI_APPLICATION = 'motorfix.asgi.application'

# ---------------------------
# DATABASE
# ---------------------------
# Default: SQLite (local development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# If DATABASE_URL is set (Render Postgres), override default
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=True
    )

# ---------------------------
# PASSWORD VALIDATION
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------
# INTERNATIONALIZATION
# ---------------------------
LANGUAGE_CODE = "en"
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('Français')),
    ('es', _('Español')),
    ('sw', _('Kiswahili')),
]
TIME_ZONE = "Africa/Nairobi"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [BASE_DIR / 'locale']

# ---------------------------
# STATIC & MEDIA
# ---------------------------
STATIC_URL = "/static/"

# Collectstatic will dump everything here (works for Render)
STATIC_ROOT = str(BASE_DIR / "staticfiles")

# Your app-level static folder (during development)
STATICFILES_DIRS = [BASE_DIR / "static"]

# Whitenoise will compress & cache static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------
# AUTH REDIRECTS
# ---------------------------
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ---------------------------
# DEFAULT PRIMARY KEY FIELD
# ---------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------
# EMAIL (development only)
# ---------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ---------------------------
# EXTRA SECURITY (for production)
# ---------------------------
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'
