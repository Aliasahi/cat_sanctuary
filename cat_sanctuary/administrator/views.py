from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from administrator.models import User
from .forms import CustomUserCreationForm 

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('role_based_redirect')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def role_based_redirect(request):
    """Redirect users to their appropriate dashboard based on role"""
    if request.user.role == 'admin':
        return redirect('administrator:dashboard')
    elif request.user.role == 'medical_staff':
        return redirect('medical_staff:dashboard')
    else:
        return redirect('caretaker:dashboard')

class RoleRequiredMixin(UserPassesTestMixin):
    required_role = None 

    def test_func(self):
        return self.request.user.role == self.required_role

# class AdminRequiredMixin(UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.role == 'admin'

# class MedicalStaffRequiredMixin(UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.role == 'medical_staff'

# class CaretakerRequiredMixin(UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.role == 'caretaker'

class ManageUsersView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = User
    template_name = 'administrator/manage_users.html'
    context_object_name = 'users'
    required_role = 'admin'

@login_required
@user_passes_test(lambda u: u.role == 'admin')
def system_config(request):
    return render(request, 'administrator/system_config.html')

class AdminDashboardView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    template_name = "administrator/dashboard.html"
    required_role = "admin"

@login_required
def medical_dashboard(request):
    if request.user.role != 'medical_staff':
        return redirect('role_based_redirect')
    return render(request, 'medical_staff/dashboard.html')

@login_required
def caretaker_dashboard(request):
    if request.user.role != 'caretaker':
        return redirect('role_based_redirect')
    return render(request, 'caretaker/dashboard.html')