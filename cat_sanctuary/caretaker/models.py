from django.db import models
from administrator.models import User

class DailyCare(models.Model):
    care_id = models.AutoField(primary_key=True)
    cat = models.ForeignKey("medical_staff.Cat", on_delete=models.CASCADE, related_name="daily_care_records")
    caretaker = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'caretaker'})
    date = models.DateField(auto_now_add=True)
    feeding_time = models.TimeField()
    food_type = models.CharField(max_length=50)
    food_amount = models.DecimalField(max_digits=5, decimal_places=2)
    behavior = models.TextField()
    grooming = models.BooleanField()
    notes = models.TextField(blank=True, null=True)  # Allows notes to be optional

    def __str__(self):
        return f"{self.cat.name} - {self.date} (Caretaker: {self.caretaker.username})"
