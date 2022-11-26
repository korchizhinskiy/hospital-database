from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from database.models import Department, \
                            Doctor, \
                            Patient, \
                            Specialization, \
                            Visit
from database.serializers import DoctorSerializer, \
                                 PatientSerializer, \
                                 VisitSerializer



class DoctorViewSet(viewsets.ModelViewSet):
    """Doctor View Set"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DoctorSerializer
    
    def get_queryset(self):
        return Doctor.objects.all().prefetch_related("chart_set").select_related(
                "doctor_specialization_id",
                "doctor_department_id",
                )

#TODO: Убрать получение departments в бизнес логику
    @action(methods=['get'], detail=False)
    def departments(self, request):
        departments = Department.objects.all()
        return Response({"departments": [department.department_name for department in departments]})

    @action(methods=['get'], detail=False)
    def specializations(self, request):
        specializations = Specialization.objects.all()
        return Response({"specializations": [specialization.specialization_name for specialization in specializations]})


class PatientViewSet(viewsets.ModelViewSet):
    """Patient View Set"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PatientSerializer

#OPTIMIZE: Оптимизаровать запросы, с desease
    def get_queryset(self):
        return Patient.objects.prefetch_related("medicalhistory_set").all()


class VisitViewSet(viewsets.ModelViewSet):
    """Chart Model View Set"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = VisitSerializer

    def get_queryset(self):
        return Visit.objects.all().select_related(
                "visit_doctor_id",
                "visit_patient_id"
                )

    
    
