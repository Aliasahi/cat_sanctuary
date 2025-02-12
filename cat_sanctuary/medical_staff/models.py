from django.db import models
from administrator.models import User

class Cat(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    intake_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Healthy', 'Healthy'), ('Sick', 'Sick'), ('Adopted', 'Adopted')])

    def __str__(self):
        return self.name

class HealthRecord(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name="health_records")
    staff = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'medical_staff'})
    date = models.DateTimeField(auto_now_add=True)
    record_type = models.CharField(max_length=30, choices=[('Checkup', 'Checkup'), ('Surgery', 'Surgery'), ('Vaccination', 'Vaccination')])
    description = models.TextField()
    treatment = models.TextField()
    medications = models.TextField(blank=True, null=True)  # Optional field
    next_checkup = models.DateField(blank=True, null=True)  # Optional field

    def __str__(self):
        return f"{self.cat.name} - {self.date} (Type: {self.record_type})"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    cat = models.ForeignKey("medical_staff.Cat", on_delete=models.CASCADE, related_name="appointments")
    staff = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'medical_staff'})
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.cat.name} - {self.date} at {self.time}"