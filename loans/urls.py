from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_loan, name='apply_loan'),
    path('success/', views.loan_success, name='loan_success'),
    path('dashboard/', views.loan_dashboard, name='loan_dashboard'),
]
