from django.urls import include, path
from rest_framework import routers

from database.views import DoctorViewSet


router = routers.SimpleRouter()
router.register(r'doctor', DoctorViewSet, basename='doctor')


urlpatterns = [
    path('api/', include(router.urls))
]
