from django.db import models


class doctorsmodel(models.Model):
    SPECIALIZATION_CHOICES = [

        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Pediatrics', 'Pediatrics'),
        ('Dermatology', 'Dermatology'),
        ('Orthopedics', 'Orthopedics'),
        ('General', 'General'),
    ]
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age  = models.PositiveIntegerField()
    specialization = models.CharField(max_length=20 , choices= SPECIALIZATION_CHOICES)
    email = models.EmailField(unique = True)
    address = models.TextField()
    licence_number = models.CharField(max_length=50 , unique = True)
    available_time_from = models.TimeField()
    available_time_to = models.TimeField()
    date_joined = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"


