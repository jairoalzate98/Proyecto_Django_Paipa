from rest_framework.pagination import PageNumberPagination


class CaracPagination(PageNumberPagination):
    ordering = 'areas'
    page_size = 50
    page_size_query_param = 'page_size'