from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Loan 
from .forms import LoanForm


# Create your views here.

@login_required
def loan_dashboard(request):
    loans = Loan.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'loans/dashboard.html', {'loans':loans})

@login_required
def apply_loan(request):
    if request.method == "POST" :
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.save()
            return redirect('loan_dashboard')
    else:
        form = LoanForm()
    return render(request, 'loans/apply.html', {'form' : form})
    
@login_required
def loan_success(request):
    return render(request, 'loans/success.html')