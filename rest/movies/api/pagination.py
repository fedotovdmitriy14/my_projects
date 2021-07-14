from rest_framework.pagination import PageNumberPagination
# add a custom class

class ReviewListPagination(PageNumberPagination):
    page_size = 1
    # page_size_query_param = 'page_size'
    max_page_size = 2