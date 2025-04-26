from django.urls import path
from Patients.views import PatientAPIView , PatientDetailAPIView

urlpatterns = [
    path('', PatientAPIView.as_view(), name='patient_list'),
    path('<int:pk>/', PatientDetailAPIView.as_view(), name='patient_detail'),
]
