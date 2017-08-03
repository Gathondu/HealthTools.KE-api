from elasticsearch_dsl import (
    DocType,
    Date,
    Keyword,
    Long,
    Text
)

from ..settings import ES
from ..elastic import Elastic


class ClinicalOfficerIndex(DocType):
    id = Long()
    name = Text(fields={'raw': Keyword()})
    reg_date = Date()
    reg_no = Text()
    valid_dates = Text()
    address = Text()
    qualifications = Text()

    class Meta:
        index = ES['index']
        doc_type = 'clinical-officers'
        using = Elastic().es_client
