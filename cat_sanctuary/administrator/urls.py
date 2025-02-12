from django.urls import path
from .views import AdminDashboardView, ManageUsersView
from . import views

app_name = 'administrator'  

urlpatterns = [
    path('dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('manage-users/', ManageUsersView.as_view(), name='manage_users'),
    path('signup/', views.signup, name='signup'),
]