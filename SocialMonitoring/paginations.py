
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class LimitsetPagination(LimitOffsetPagination):
    pass






# class CustomPagination(pagination.PageNumberPagination):
#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'results': data
#         })


# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000