from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import PatientDoctorMapping
from .serializers import patientdoctermappingserializer
from django.shortcuts import get_object_or_404

class PatientDoctorMappingView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        serializer = patientdoctermappingserializer(mappings, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = patientdoctermappingserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Mapping created successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PatientDoctorMappingDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, patient_id=None):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        if not mappings.exists():
            return Response({"error": "No mappings found for this patient."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = patientdoctermappingserializer(mappings, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        mapping = get_object_or_404(PatientDoctorMapping, id=id)
        mapping.delete()
        return Response({"message": "Mapping deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
