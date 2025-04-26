from django.urls import path
from .views import PatientDoctorMappingView , PatientDoctorMappingDetailView

urlpatterns = [
    path('', PatientDoctorMappingView.as_view(), name='doctor_list'),
    path('<int:id>/', PatientDoctorMappingDetailView.as_view(), name='doctor_detail'),
]
