from rest_framework.response import Response
from rest_framework import status

from .exceptions import SiteNotFoundException
from .models import Site


class SiteMiddleware:

    REPLACE_WITH_WWW = ['localhost', 'bidici', '127']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        sub = request.META['HTTP_HOST'].split('.')[0].split(':')[0]
        if sub in self.REPLACE_WITH_WWW:
            sub = 'www'

        try:
            request.site = Site.objects.get(sub_domain=sub)
        except Site.DoesNotExist as ex:
            ex = SiteNotFoundException()
            data = {'detail': ex.detail}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        return None

