from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import doctorsmodel
from .serializers import doctorsserializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class DoctorAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        if id:
            doctor = get_object_or_404(doctorsmodel, id=id)
            serializer = doctorsserializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Retrieve all doctors
            doctors = doctorsmodel.objects.all()
            serializer = doctorsserializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = doctorsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        doctor = get_object_or_404(doctorsmodel, id=id)
        serializer = doctorsserializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        doctor = get_object_or_404(doctorsmodel, id=id)
        doctor.delete()
        return Response({'message': 'Doctor deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
