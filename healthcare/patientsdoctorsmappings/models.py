from django.db import models
from Patients.models import patientmodel  
from doctors.models import doctorsmodel    


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(patientmodel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctorsmodel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Patient: {self.patient} - Doctor: {self.doctor}"

