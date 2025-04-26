from rest_framework import serializers
from .models import patientmodel

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = patientmodel
        fields = '__all__'

        read_only_fields = ['user']
