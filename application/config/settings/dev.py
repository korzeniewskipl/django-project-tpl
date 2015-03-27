from os.path import join

from config.settings.common import CommonSettings
from config.settings.mixins import DebugToolbar


class Settings(
    DebugToolbar,
    CommonSettings,
):

    @property
    def ADMINS(self):
        return [
            ('Paweł Korzeniewski', 'pawel@korzeniewski.pl'),
        ]

    @property
    def ALLOWED_HOSTS(self):
        return []

    @property
    def DATABASES(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': join(self.SITE_DIR, 'db', 'django.sqlite3'),
                # 'USER': 'vagrant',
                # 'PASSWORD': 'vagrant',
                # 'HOST': '127.0.0.1',
                # 'PORT': '5432',
                # 'CONN_MAX_AGE': 600,
            }
        }

    @property
    def DEBUG(self):
        return True

    @property
    def MANAGERS(self):
        return self.ADMINS

    @property
    def SECRET_KEY(self):
        return '^)*91j10k@i0!_+013ncsl=lfs5405+)1-rer27#d4a)c59el&'


Settings.install()
