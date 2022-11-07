from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from database.utils import GetDoctorDataMixin, GetPatientDataMixin

from .models import Doctor, Patient, Visit


def home_page(request):
    return render(request, 'database/main_page.html')

class DoctorsListView(ListView):
    """Doctor List View"""
    model = Doctor
    allow_empty = False
    template_name = 'database/doctors_list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        """Get all Doctors with their departments and specializations"""
        doctors = Doctor.objects.select_related(
                                                'doctor_department_id',
                                                'doctor_specialization_id'
                                                ).all()
        return doctors


class DoctorDetailView(GetDoctorDataMixin, DetailView):
    """Doctor Detail View"""
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'database/doctor.html'

    def get_queryset(self):
        return Doctor.objects.filter(
                pk=self.kwargs['pk']
                ).select_related('doctor_specialization_id', 
                                 'doctor_department_id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chart = self.get_doctor_chart(doctor_id=self.kwargs['pk'])
        visit = self.get_doctor_visit(doctor_id=self.kwargs['pk'])
        return context | chart | visit


class PatientsListView(ListView):
    """Patient List View"""
    model = Patient
    allow_empty = False
    template_name = 'database/patients_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        """Get all Patients """
        patients = Patient.objects.order_by('patient_last_name',
                                            'patient_first_name').all()
        return patients


class PatientDetailView(GetPatientDataMixin, DetailView):
    """Patient Detail View"""
    model = Patient
    context_object_name = 'patient'
    template_name = 'database/patient.html'

    def get_queryset(self):
        return Patient.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medical_history = self.get_patient_medical_history(self.kwargs['pk'])
        visit = self.get_doctor_visit_by_patient(self.kwargs['pk'])
        return context | medical_history | visit

class VisitDetailView(DetailView):
    """Visit Detail View"""
    model = Visit
    context_object_name = 'visit'
    template_name = 'database/visit.html'
    
    def get_queryset(self):
        return Visit.objects.filter(visit_id=self.kwargs['pk']
                                    ).select_related('visit_patient_id',
                                                     'visit_doctor_id')



