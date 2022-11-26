from django.urls import include, path
from rest_framework import routers

from database.views import DoctorViewSet, \
                           PatientViewSet, \
                           VisitViewSet



router = routers.SimpleRouter()
router.register(r'doctor', DoctorViewSet, basename='doctor')
router.register(r'patient', PatientViewSet, basename='patient')
router.register(r'visit', VisitViewSet, basename='visit')


urlpatterns = [
    path('api/', include(router.urls))
]
