from django.db import models

class PaymentType(models.Model):

      # Choices for the new transaction_type field
    TRANSACTION_TYPE_CHOICES = [
        ('SNA', 'SNA'),
        ('NON_SNA', 'NON SNA'),
        ('CNA', 'CNA'),
    ]

    PAYMENT_CHOICES = (
        ('RTGS', 'RTGS'),
        ('NEFT', 'NEFT'),
        ('ABS', 'ABS'), # Assuming ABS stands for something like 'Aadhaar Based Services'
        ('CHEQUE', 'Cheque'),
    )
   # New field: Transaction Type
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        default='SNA', # Or a suitable default
        verbose_name="Transaction Type"
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
        verbose_name = "Payment Type"
        verbose_name_plural = "Payment Types"

    def __str__(self):
        return f"({self.get_payment_type_display()}) ({self.get_transaction_type_display()})"

    def get_transaction_type_display(self):
        # Helper to get human-readable choice for transaction_type
        return dict(self.TRANSACTION_TYPE_CHOICES).get(self.transaction_type, self.transaction_type)