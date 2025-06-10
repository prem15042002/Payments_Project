from django.db import models

class PaymentType(models.Model):
    PAYMENT_CHOICES = (
        ('RTGS', 'RTGS'),
        ('NEFT', 'NEFT'),
        ('ABS', 'ABS'), # Assuming ABS stands for something like 'Aadhaar Based Services'
        ('CHEQUE', 'Cheque'),
    )

    payment_type = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICES,
        unique=True
    )

    # New field for account number
    # blank=True means it's not required in forms
    # null=True means it can be NULL in the database
    account_number = models.CharField(max_length=20, blank=True, null=True)

    # New field for Aadhaar number
    aadhar_number = models.CharField(max_length=12, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.get_payment_type_display()