from django.forms import ModelForm
from django.forms.widgets import DateTimeInput
from .models import Visit


class VisitForm(ModelForm):
    """Visit Form of doctor's appointment"""
    class Meta:
        model = Visit
        fields = (
                "visit_doctor_id",
                "visit_patient_id",
                "visit_datetime",
                )
        widgets = {
                'visit_datetime': DateTimeInput(attrs={'type': 'datetime-local'})
                }
    
