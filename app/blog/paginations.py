from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class PostOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class PostNumberPagination(PageNumberPagination):
    page_size = 3
