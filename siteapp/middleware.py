from .exceptions import InvalidSiteException
from .models import Site


class SiteMiddleware:

    REPLACE_WITH_WWW = ['localhost', 'bidici', '127']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        sub = request.META['HTTP_HOST'].split('.')[0].split(':')[0]
        if sub in self.REPLACE_WITH_WWW:
            sub = 'www'

        try:
            request.site = Site.objects.get(sub_domain=sub)
        except Site.DoesNotExist as e:
            raise InvalidSiteException from e

        response = self.get_response(request)
        return response
