from django.contrib import admin
from .models import Doctor, \
                   Patient, \
                   Department, \
                   Specialization, \
                   Chart, \
                   Schedule, \
                   MedicalHistory, \
                   DeseaseRecipe, \
                   DoctorVisit, \
                   WorkTime

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Doctor Admin Model"""
    pass

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Patient Admin Model"""
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Department Admin Model"""
    pass
                    
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """Specialization Admin Model"""
    pass

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    """Chart Admin Model"""
    pass
            
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Schedule Admin Model"""
    pass

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    """Medical History Admin Model"""
    pass

@admin.register(DeseaseRecipe)
class DeseaseRecipeAdmin(admin.ModelAdmin):
    """Desease Recipe Admin Model"""
    pass

@admin.register(DoctorVisit)
class DoctorVisitAdmin(admin.ModelAdmin):
    """Doctor Visit Admin Model"""
    pass

@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    """Work Time Admin Model"""
    pass
