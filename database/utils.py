from .models import Chart


class GetDataMixin:
    """Abstract class"""


class GetDoctorDataMixin(GetDataMixin):
    """Get data class for doctor"""
    def get_doctor_chart(self, doctor_id, **kwargs):
        context = kwargs
        chart = Chart.objects.filter(chart_doctor_id=doctor_id)
        context['chart'] = chart
        return context
