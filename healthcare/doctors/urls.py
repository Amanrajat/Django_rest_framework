from django.urls import path
from .views import DoctorAPIView

urlpatterns = [
    path('', DoctorAPIView.as_view(), name='doctor_list'),
    path('<int:id>/', DoctorAPIView.as_view(), name='doctor_detail'),
]
