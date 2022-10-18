from .models import Chart, Visit, MedicalHistory


class GetDataMixin:
    """Abstract class"""


class GetDoctorDataMixin(GetDataMixin):
    """Get data class for doctor"""

    def get_doctor_chart(self, doctor_id, **kwargs):
        """Get doctor's work chart"""
        context = kwargs
        chart = Chart.objects.filter(chart_doctor_id=doctor_id)
        context['chart'] = chart
        return context

        #TODO: Сделать декоратор на посещение
    def get_doctor_visit(self, doctor_id, **kwargs):
        """Get doctor's future visit"""
        context = kwargs
        visit = Visit.objects.filter(visit_doctor_id=doctor_id)
        context['visit'] = visit
        return context


class GetPatientDataMixin(GetDataMixin):
    """Get data class for patient"""
    def get_patient_medical_history(self, patient_id, **kwargs):
        """Get patient's medical history"""
        context = kwargs
        medical_history = MedicalHistory.objects.filter(
                medical_patient_id=patient_id)
        context['medical_history'] = medical_history
        return context

    def get_doctor_visit_by_patient(self, patient_id, **kwargs):
        """Get doctor's visit by patient"""
        context = kwargs
        visit = Visit.objects.filter(visit_patient_id=patient_id)
        context['visit'] = visit
        return context
