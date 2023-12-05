from django import get_version
from django.conf import settings


HEADER = getattr(settings, 'X_POWERED_BY', 'Django/%(version)s') % {'version': get_version()}

class XPoweredByMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        response['X-Powered-By'] = HEADER

        return response
