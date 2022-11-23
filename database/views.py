from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from database.models import Department, Doctor
from database.serializers import DoctorSerializer



class DoctorViewSet(viewsets.ModelViewSet):
    """Doctor View Set"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DoctorSerializer
    
    def get_queryset(self):
        return Doctor.objects.all().select_related(
                "doctor_specialization_id",
                "doctor_department_id",
                )

#TODO: Убрать получение departments в бизнес логику
    @action(methods=['get'], detail=False)
    def departments(self, request):
        departments = Department.objects.all()
        return Response({"departments": [department.department_name for department in departments]})
    
