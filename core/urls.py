from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home , name='home'   ),
    path('personal_loan/', views.personal_loan, name='personal_loan' ),
    path('business_loan/' , views.business_loan, name='business_loan'),
    
]
