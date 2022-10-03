from django.contrib import admin
from .models import Department, \
                    Specialization, \
                    Day, \
                    WorkTime, \
                    Chart, \
                    Doctor, \
                    Schedule,\
                    Recipe, \
                    Desease, \
                    MedicalHistory, \
                    Patient, \
                    Visit


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Department Admin Model"""
    pass

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """Specialization Admin Model"""
    pass

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    """Day Admin Model"""
    pass

@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    """Work Time Admin Model"""
    pass

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    """Chart Admin Model"""
    pass

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Specialization Admin Model"""
    pass

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Specialization Admin Model"""
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Recipe Admin Model"""
    pass

@admin.register(Desease)
class DeseaseAdmin(admin.ModelAdmin):
    """Desease Admin Model"""
    pass

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    """Medical History Admin Model"""
    pass

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Patient Admin Model"""
    pass

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """Visit Admin Model"""
    pass
