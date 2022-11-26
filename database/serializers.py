from rest_framework import serializers

from database.models import Chart, \
                            Department, \
                            Desease, \
                            Doctor, \
                            MedicalHistory, \
                            Patient, \
                            Specialization, \
                            Visit

                            

class SpecializationSerializer(serializers.ModelSerializer):
    """Specialization Serializer"""

    class Meta:
        model = Specialization
        fields = (
                "specialization_name",
                )


class DepartmentSerializer(serializers.ModelSerializer):
    """Department Serializer"""

    class Meta:
        model = Department
        fields = (
                "department_name",
                )
        

class ChartSerializer(serializers.ModelSerializer):
    """Chart Serializer"""
    
    class Meta:
        model = Chart
        fields = (
                "chart_day_id",
                "chart_work_time_start",
                "chart_work_time_end",
                )
    

class DoctorSerializer(serializers.ModelSerializer):
    """Doctor Serializer"""
    doctor_specialization_id = SpecializationSerializer()
    doctor_department_id = DepartmentSerializer()
    doctor_chart = ChartSerializer(source="chart_set", many=True)
    
    class Meta:
        model = Doctor
        fields = (
                "doctor_last_name",
                "doctor_first_name",
                "doctor_second_name",
                "doctor_age",
                "doctor_department_id",
                "doctor_specialization_id",
                "doctor_chart"
                )


class DeseaseSerializer(serializers.ModelSerializer):
    """Desease Serializer"""

    class Meta:
        model = Desease
        fields = (
                "desease_name",
                "recipe_text",
                )
    

class MedicalHistorySerializer(serializers.ModelSerializer):
    """Medical History Serializer"""
    medical_history_desease_id = DeseaseSerializer()

    class Meta:
        model = MedicalHistory
        fields = (
                "medical_history_start",
                "medical_history_end",
                "medical_history_desease_id",
                )


class PatientSerializer(serializers.ModelSerializer):
    """Patient Serializer"""
    medical_history = MedicalHistorySerializer(source="medicalhistory_set", many=True)

    class Meta:
        model = Patient
        fields = (
                "patient_last_name",
                "patient_first_name",
                "patient_second_name",
                "patient_age",
                "medical_history",
                )


class VisitSerializer(serializers.ModelSerializer):
    """Visit Serializer"""
    visit_doctor_id = DoctorSerializer()
    visit_patient_id = PatientSerializer()

    class Meta:
        model = Visit
        fields = (
                "visit_doctor_id",
                "visit_patient_id",
                "visit_datetime",
                )
    
