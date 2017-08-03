from django.conf.urls import url

from views import (doctors, nurses, health_facilities,
                   nhif, sms_handler)

urlpatterns = [
    url(r'^doctors/$', doctors.index),
    url(r'^doctors/search.json', doctors.search),
    url(r'^nurses/$', nurses.index),
    url(r'^nurses/search.json', nurses.search),
    url(r'^health-facilities/$', health_facilities.index),
    url(r'^health-facilities/search.json', health_facilities.search),
    url(r'^nhif/$', nhif.index),
    url(r'^nhif/inpatient/$', nhif.index),
    url(r'^nhif/outpatient-cs/$', nhif.index),
    url(r'^nhif/outpatient/$', nhif.index),
    url(r'^nhif/outpatient-cs/search.json', nhif.search_outpatient_cs),
    url(r'^nhif/outpatient/search.json', nhif.search_outpatient),
    url(r'^nhif/inpatient/search.json', nhif.search_inpatient),
    url(r'^sms/', sms_handler.sms),
]
