from django.shortcuts import render , get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from .models import patientmodel
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PatientSerializer
from django.core.exceptions import ObjectDoesNotExist


class PatientAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            patients = patientmodel.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request):
        try:
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


   
class PatientDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return patientmodel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request,pk):
        try:
            patient = self.get_object(pk)
            if patient is None:
                return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            patient = self.get_object(pk)
            if patient is None:
                return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = PatientSerializer(patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            patient = self.get_object(pk)
            if patient is None:
                return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)
            patient.delete()
            return Response({"message": "Patient deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


