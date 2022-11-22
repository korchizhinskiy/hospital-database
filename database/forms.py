from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.widgets import DateTimeInput
from .models import Visit

from .utils import get_doctor_worktime



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

    #TODO: Check day of week
    def clean_visit_datetime(self):
        """Validate the DateTime of the appointment to the doctor"""
        doctor_id = self.cleaned_data['visit_doctor_id']
        input_datetime = self.cleaned_data['visit_datetime']

        
        worktime = get_doctor_worktime(doctor_id)

        if not worktime['doctor_worktime_start'] <= input_datetime.time() <= worktime['doctor_worktime_end']:
            raise ValidationError("В это время врач не работает")

        return input_datetime

