from django.contrib import admin
from .models import Cat, HealthRecord, Appointment

admin.site.register(Cat)
admin.site.register(HealthRecord)
admin.site.register(Appointment)
