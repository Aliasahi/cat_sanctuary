from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.mixins import RoleRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from caretaker.models import DailyCare
from medical_staff.models import Cat

class CaretakerDashboardView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    template_name = "caretaker/dashboard.html"
    required_role = "caretaker"

class DailyCareListView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = DailyCare
    template_name = 'caretaker/daily_care.html'
    context_object_name = 'daily_cares'
    required_role = 'caretaker'

@login_required
def add_care_record(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)  
    if request.method == 'POST':
        # Add form processing logic here
        pass
    cat = Cat.objects.get(pk=cat_id)
    return render(request, 'caretaker/add_care_record.html', {'cat': cat})