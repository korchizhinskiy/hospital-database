from rest_framework import serializers

from database.models import Department, \
                            Doctor, \
                            Specialization

                            

class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields = (
                "specialization_name",
                )


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = (
                "department_name",
                )
        
    

class DoctorSerializer(serializers.ModelSerializer):
    """Doctor Serializer"""
    doctor_specialization_id = SpecializationSerializer()
    doctor_department_id = DepartmentSerializer()
    
    class Meta:
        model = Doctor
        fields = (
                "doctor_last_name",
                "doctor_first_name",
                "doctor_second_name",
                "doctor_age",
                "doctor_department_id",
                "doctor_specialization_id",
                )
        
