import sys
from abc import ABCMeta, abstractmethod
from os.path import abspath, dirname, join


class Settings(metaclass=ABCMeta):

    ROOT_DIR = abspath(join(dirname(__file__), '..', '..', '..'))
    SITE_DIR = join(ROOT_DIR, 'site')
    BASE_DIR = join(ROOT_DIR, 'application')
    APPS_DIR = join(BASE_DIR, 'apps')

    @classmethod
    def install(cls):
        sys.modules[cls.__module__] = inst = cls()
        try:
            sys.path.index(inst.APPS_DIR)
        except ValueError:
            sys.path.insert(1, inst.APPS_DIR)


class Admins(Settings):

    @property
    @abstractmethod
    def ADMINS(self):
        return [
            ('Your Name', 'your_email@example.com'),
        ]

    @property
    @abstractmethod
    def MANAGERS(self):
        return [
            ('Your Name', 'your_email@example.com'),
        ]


class Apps(Settings):

    @property
    def DJANGO_APPS(self):
        return [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]

    @property
    def THIRD_PARTY_APPS(self):
        return []

    @property
    def PROJECT_APPS(self):
        return [
            'common',
        ]

    @property
    def INSTALLED_APPS(self):
        return self.DJANGO_APPS + self.THIRD_PARTY_APPS + self.PROJECT_APPS


class Assets(Settings):
    """Static files (CSS, JavaScript, Images)

    https://docs.djangoproject.com/en/dev/howto/static-files/
    """

    @property
    def MEDIA_URL(self):
        return '/media/'

    @property
    def STATIC_URL(self):
        return '/static/'

    @property
    def MEDIA_ROOT(self):
        """Absolute filesystem path to the directory that will hold user-uploaded files."""
        return join(self.SITE_DIR, 'media')

    @property
    def STATIC_ROOT(self):
        """Absolute filesystem path to the directory static files should be collected to."""
        return join(self.SITE_DIR, 'static')

    @property
    def STATICFILES_DIRS(self):
        return [
            join(self.BASE_DIR, 'static'),
        ]


class Auth(Settings):

    @property
    def AUTH_PASSWORD_VALIDATORS(self):
        return []


class Database(Settings):

    @property
    @abstractmethod
    def DATABASES(self):
        pass


class I18N(Settings):
    """Internationalization and localization

    https://docs.djangoproject.com/en/dev/topics/i18n/
    """

    TIME_ZONE = 'UTC'

    LANGUAGE_CODE = 'en-us'

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True


class Logging(Settings):
    """
    A sample logging configuration. The only tangible logging
    performed by this configuration is to send an email to
    the site admins on every HTTP 500 error when DEBUG=False.
    See http://docs.djangoproject.com/en/dev/topics/logging for
    more details on how to customize your logging configuration.
    """

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }


class Middleware(Settings):

    @property
    def MIDDLEWARE_CLASSES(self):
        # TODO: https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-middleware
        return [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]


class Secrets(Settings):

    @property
    @abstractmethod
    def SECRET_KEY(self):
        pass


class Site(Settings):

    ROOT_URLCONF = 'config.urls'
    SITE_ID = 1

    @property
    @abstractmethod
    def ALLOWED_HOSTS(self):
        pass


class Templates(Settings):

    @property
    def TEMPLATES(self):
        return [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    join(self.BASE_DIR, 'templates'),
                ],
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


class Wsgi(Settings):

    WSGI_APPLICATION = 'config.wsgi.application'


# Assemble all subclasses of 'Settings' into 'CommonSettings' class.
CommonSettings = type(
    'CommonSettings',
    tuple([cls for cls in Settings.__subclasses__() if cls.__module__ == __name__]),
    {}
)
