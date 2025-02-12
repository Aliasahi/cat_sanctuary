from django.db import models

# Create your models here.

# administrator/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ('admin', 'Administrator'),
        ('medical', 'Medical Staff'),
        ('caretaker', 'Caretaker'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(null=True)
    status = models.BooleanField(default=True)  # active/inactive
    def is_administrator(self):
        return self.role == self.Roles.ADMINISTRATOR

    def is_medical_staff(self):
        return self.role == self.Roles.MEDICAL_STAFF

    def is_caretaker(self):
        return self.role == self.Roles.CARETAKER
