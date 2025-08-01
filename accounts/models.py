from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICE = (
        ('customer', 'Customer'),
        ('officer', 'Loan Officer'),
        ('admin', 'Admin'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default='customer')
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(blank=True)
    kyc_document = models.FileField(upload_to='kyc_docs/',blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"