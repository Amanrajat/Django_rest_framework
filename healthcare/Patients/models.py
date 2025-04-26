from django.db import models

class patientmodel(models.Model):
    GENDER_CHOICES =[
          ('M' , 'Male'),
          ('F','Female'),
          ('O','Other'),
    ]
          
     
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1 , choices=GENDER_CHOICES)
    contact = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
