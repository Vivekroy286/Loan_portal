from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Loan


# Create your views here.

@login_required
def loan_dashboard(request):
    loans = Loan.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'loan/dashboard.html', {'loans':loans})
