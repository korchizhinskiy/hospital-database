from django.contrib import admin
from .models import Department, \
                    Specialization, \
                    Chart, \
                    Doctor, \
                    Day, \
                    Desease, \
                    MedicalHistory, \
                    Patient, \
                    Visit


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Department Admin Model"""
    search_fields = ('department_name',)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """Specialization Admin Model"""
    search_fields = ('specialization_name',)


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    """Day Admin Model"""


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    """Chart Admin Model"""
    list_display = (
                    'get_full_name',
                    'chart_day_id',
                    'chart_work_time_start',
                    'chart_work_time_end'
            )
    search_fields = (
                     'chart_doctor_id__doctor_last_name',
                     'chart_doctor_id__doctor_first_name',
                     'chart_day_id__day_name'
                    )

    def get_full_name(self, chart):
        return f"{chart.chart_doctor_id.doctor_last_name}" \
               f" {chart.chart_doctor_id.doctor_first_name}" \
               f" {doctor_second_name if(doctor_second_name := chart.chart_doctor_id.doctor_second_name) else ''}"


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Specialization Admin Model"""
    list_display = (
                    'get_full_name',
                    'get_department_name',
                    'get_specialization_name',
                    'doctor_experience',
                    )
    search_fields = (
                     'doctor_last_name',
                     'doctor_first_name',
                    )

    @admin.display(description='Врач')
    def get_full_name(self, doctor):
        return f"{doctor.doctor_last_name} {doctor.doctor_first_name}" \
               f" {doctor.doctor_second_name if doctor.doctor_second_name else ''}"

    @admin.display(description='Отделение')
    def get_department_name(self, doctor):
        return f"{doctor.doctor_department_id.department_name}"

    @admin.display(description='Специальность')
    def get_specialization_name(self, doctor):
        return f"{doctor.doctor_specialization_id.specialization_name}"


@admin.register(Desease)
class DeseaseAdmin(admin.ModelAdmin):
    """Desease Admin Model"""
    list_display = (
                    'desease_name',
                    'recipe_text'
                    )


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    """Medical History Admin Model"""
    list_display = (
                    'get_full_name',
                    'get_patient_desease',
                    'medical_history_start',
                    'medical_history_end'

            )
    search_fields = (
                     'medical_history_patient_id__patient_last_name',
                     'medical_history_patient_id__patient_first_name'
                    )

    @admin.display(description='Пациент')
    def get_full_name(self, medical_history):
        return f"{medical_history.medical_patient_id.patient_first_name}" \
               f" {medical_history.medical_patient_id.patient_last_name}"

    @admin.display(description='Диагноз')
    def get_patient_desease(self, medical_history):
        return f"{medical_history.medical_history_desease_id.desease_name}"


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Patient Admin Model"""
    list_display = (
                    'get_full_name',
                    'patient_age'
                    )
    search_fields = (
                     'patient_last_name',
                     'patient_first_name'
                    )

    @admin.display(description='Пациент')
    def get_full_name(self, patient):
        return f"{patient.patient_last_name} {patient.patient_first_name}" \
                f" {patient_second_name if (patient_second_name := patient.patient_second_name) else ''}"


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """Visit Admin Model"""
    list_display = (
                    'get_doctor_full_name',
                    'get_patient_full_name',
                    'visit_datetime'
                    )
    search_fields = (
                     'visit_doctor_id__doctor_last_name',
                     'visit_patient_id__patient_last_name'
                    )

    @admin.display(description='Врач')
    def get_doctor_full_name(self, visit):
        return f"{visit.visit_doctor_id.doctor_last_name} {visit.visit_doctor_id.doctor_first_name}" \
               f" {doctor_second_name if (doctor_second_name := visit.visit_doctor_id.doctor_second_name) else ''}"

    @admin.display(description='Пациент')
    def get_patient_full_name(self, visit):
        return f"{visit.visit_patient_id.patient_last_name} {visit.visit_patient_id.patient_first_name}" \
               f" {patient_second_name if (patient_second_name := visit.visit_patient_id.patient_second_name) else ''}"
