from rest_framework_elasticsearch import es_views, es_pagination, es_filters

from .index import ClinicalOfficerIndex
from ..elastic import Elastic


class ClinicalOfficerView(es_views.ListElasticAPIView):
    es_client = Elastic().es_client
    es_paginator = es_pagination.ElasticLimitOffsetPagination()
    es_model = ClinicalOfficerIndex
    es_filter_backends = (
        es_filters.ElasticSearchFilter,
        es_filters.ElasticFieldsFilter,
        es_filters.ElasticOrderingFilter,
    )
    # import pdb; pdb.set_trace()
    # es_ordering = 'id'
    # es_search_fields = ('name',)
    # es_filter_fields = (es_filters.ESFieldFilter('name'),)
