
class DebugToolbar:

    @property
    def THIRD_PARTY_APPS(self):
        return super(DebugToolbar, self).THIRD_PARTY_APPS + [
            'debug_toolbar',
        ]

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(DebugToolbar, self).MIDDLEWARE_CLASSES + [
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]
