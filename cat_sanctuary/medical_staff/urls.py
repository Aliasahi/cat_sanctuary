from django.urls import path
from .views import MedicalDashboardView, HealthRecordListView

app_name = 'medical_staff'

urlpatterns = [
    path('dashboard/', MedicalDashboardView.as_view(), name='medical_dashboard'),
    path('health-records/', HealthRecordListView.as_view(), name='healthrecord_list'),
]
