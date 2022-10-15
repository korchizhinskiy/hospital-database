from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Doctor, Patient

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

class DoctorDetailView(DetailView):
    """Doctor Detail View"""
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'database/doctor.html'

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

class PatientDetailView(DetailView):
    """Patient Detail View"""
    model = Patient
    context_object_name = 'patient'
    template_name = 'database/patient.html'
