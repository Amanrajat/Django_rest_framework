from rest_framework import serializers
from .models import PatientDoctorMapping


class patientdoctermappingserializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ['user']

