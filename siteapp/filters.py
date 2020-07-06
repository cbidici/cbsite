from rest_framework.filters import BaseFilterBackend


class SiteFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(site=request.site)
