from rest_framework.pagination import PageNumberPagination

class DynamicPageNumberPagination(PageNumberPagination):
     page_query_param='pageNo'
     page_size_query_param='page_size'