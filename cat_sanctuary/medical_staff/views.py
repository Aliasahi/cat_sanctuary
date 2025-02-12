from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.views import RoleRequiredMixin
from django.views.generic import ListView, CreateView
from .models import HealthRecord
from .models import Cat, HealthRecord

class MedicalDashboardView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    template_name = "medical_staff/dashboard.html"
    required_role = "medical_staff"

class HealthRecordListView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = HealthRecord
    template_name = 'medical_staff/health_records.html'
    context_object_name = 'records'
    required_role = 'medical_staff'

    def get_queryset(self):
        return HealthRecord.objects.filter(staff=self.request.user)

@login_required
def add_health_record(request, cat_id):
    if request.method == 'POST':
        # Add form processing logic here
        pass
    cat = Cat.objects.get(pk=cat_id)
    return render(request, 'medical_staff/add_health_record.html', {'cat': cat})