from django.urls import path
from . import views

app_name = "caretaker"  

urlpatterns = [
    path('dashboard/', views.CaretakerDashboardView.as_view(), name='dashboard'),
    path('daily-care/', views.DailyCareListView.as_view(), name='daily_care'),
    path('add-care/<int:cat_id>/', views.add_care_record, name='add_care_record'),
]

