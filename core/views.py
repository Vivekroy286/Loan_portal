from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def personal_loan(request):
    return render(request, 'core/personal_loan.html')

def business_loan(request):
    return render(request, 'core/business_loan.html')