from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class SiteNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('Site Not found.')
    default_code = 'site_not_found'
