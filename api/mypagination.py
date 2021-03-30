from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# class MyPageNPagination(PageNumberPagination):
#     page_size = 2
#     page_query_param ='p'
#     page_size_query_param = 'records'
#     max_page_size = 7

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'ml'
    offset_query_param = 'of'
    max_limit = 7