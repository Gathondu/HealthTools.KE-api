from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from .models import ClinicalOfficer
from .index import ClinicalOfficerIndex


class ElasticClinicalOfficerSerializer(ElasticModelSerializer):
    class Meta:
        model = ClinicalOfficer
        es_model = ClinicalOfficerIndex
        fields = ('id', 'name', 'reg_date', 'reg_no', 'valid_dates', 'address', 'qualifications')
