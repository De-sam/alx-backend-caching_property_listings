import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Basic ---
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
DEBUG = os.getenv("DEBUG", "1") == "1"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# --- Apps ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party
    "django_redis",

    # local
    "properties",
    "properties.apps.PropertiesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "alx_backend_caching_property_listings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "alx_backend_caching_property_listings.wsgi.application"

# --- Database (PostgreSQL in Docker) ---
# If you're running Django on the HOST (not in Docker), use the published port on localhost.
# If later you dockerize Django in the same compose, set HOST to 'postgres'.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "property_db"),
        "USER": os.getenv("DB_USER", "property_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "property_pass"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),  # or "postgres" if Django runs in Docker
        "PORT": int(os.getenv("DB_PORT", "5432")),
    }
}

# --- Redis cache backend ---
# Works from host via localhost:6379; if Django is in Docker, set REDIS_URL to redis://redis:6379/1
REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/1")
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Optional: better timeouts/retries (left minimal here)
        },
        "TIMEOUT": None,  # default: never expire unless set in code; we'll set per-use
    }
}

# Optional: store sessions in cache for perf (not required by the task)
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

# --- i18n / static ---
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Lagos"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
