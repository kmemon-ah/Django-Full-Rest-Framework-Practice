from rest_framework.pagination import PageNumberPagination

class MyPageNPagination(PageNumberPagination):
    page_size = 2
    page_query_param ='p'
    page_size_query_param = 'records'
    max_page_size = 7