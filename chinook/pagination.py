from rest_framework.pagination import PageNumberPagination


class TrackPagination(PageNumberPagination):

    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 300

