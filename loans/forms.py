from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['amount', 'tenure_months', 'interest_rate']
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
            'tenure_months': forms.NumberInput(attrs={'placeholder': 'Tenure in months'}),
            'interest_rate': forms.NumberInput(attrs={'placeholder': 'Interest rate %'}),
        }
