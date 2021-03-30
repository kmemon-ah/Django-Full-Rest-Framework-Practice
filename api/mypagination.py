from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# For page Number Pagination
# class MyPageNPagination(PageNumberPagination):
#     page_size = 2
#     page_query_param ='p'
#     page_size_query_param = 'records'
#     max_page_size = 7


# For Limit Offset Pagination
# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 4
#     limit_query_param = 'ml'
#     offset_query_param = 'of'
#     max_limit = 7


# For Cursor Pagination
class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cu'