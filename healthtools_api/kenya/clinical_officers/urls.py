from django.conf.urls import url

from .views import ClinicalOfficerView

urlpatterns = [
    url(
        regex=r'clinical-officers',
        view=ClinicalOfficerView.as_view(),
        name='clinical-officers'
    )
]
