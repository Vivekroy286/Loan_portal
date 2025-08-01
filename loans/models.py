from django.db import models
from django.contrib.auth.models import User

class Loan(models.Model):
    STATUS_CHOICE = (
        ('pending','Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('disbursed','Disbursed'),
        
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenure_months = models.PositiveIntegerField()
    interest_rate = models.DecimalField(max_digits=5,decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.status}"
    
    
class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_on = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"Loan {self.loan.id} - Due: {self.due_date} - Paid: {self.is_paid}"