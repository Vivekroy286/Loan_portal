from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_loan, name='apply_loan'),
    path('success/', views.loan_success, name='Loan_success'),
    path('dashboard/', views.loan_dashboard, name='Loan_dashboard'),
]
