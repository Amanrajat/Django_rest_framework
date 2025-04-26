from rest_framework import serializers
from .models import doctorsmodel

class doctorsserializer(serializers.ModelSerializer):
    class Meta:
        model = doctorsmodel
        fields = '__all__'
        read_only_fields = ['user']
