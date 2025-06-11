# payments/forms.py
from django import forms
from .models import PaymentType

class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ['transaction_type', 'payment_type', 'account_number', 'aadhar_number', 'is_active']
        # Ensure 'transaction_type' is listed here

    # Custom validation method for the entire form
    def clean(self):
        # Call the parent clean method to get cleaned data
        cleaned_data = super().clean()

        payment_type = cleaned_data.get('payment_type')
        account_number = cleaned_data.get('account_number')
        aadhar_number = cleaned_data.get('aadhar_number')

        # Clear existing errors on the fields if they are not relevant to avoid confusion
        if 'account_number' in self.errors:
            del self.errors['account_number']
        if 'aadhar_number' in self.errors:
            del self.errors['aadhar_number']

        # Logic for RTGS, NEFT, Cheque (requires account_number)
        if payment_type in ['RTGS', 'NEFT', 'CHEQUE']:
            # Account Number Validation
            if not account_number:
                self.add_error('account_number', 'Account number is required for this payment type.')
            elif not account_number.isdigit(): # Check if it's purely digits
                self.add_error('account_number', 'Account number must contain only digits.')
            elif not (10 <= len(account_number) <= 20): # Example length validation
                self.add_error('account_number', 'Account number must be between 10 and 20 digits.')

            # Ensure Aadhar number is NOT provided for these types
            if aadhar_number:
                self.add_error('aadhar_number', 'Aadhaar number should not be provided for this payment type.')

        # Logic for ABS (requires aadhar_number)
        elif payment_type == 'ABS':
            # Aadhaar Number Validation
            if not aadhar_number:
                self.add_error('aadhar_number', 'Aadhaar number is required for ABS payment type.')
            # Aadhaar numbers are typically 12 digits and numeric
            elif not (aadhar_number.isdigit() and len(aadhar_number) == 12):
                self.add_error('aadhar_number', 'Aadhaar number must be a 12-digit number.')
            # Optional: Basic Aadhaar checksum validation (Luhn algorithm or Verhoeff) is more complex.
            # For simplicity, we'll stick to digit count and numeric for now.

            # Ensure Account number is NOT provided for ABS
            if account_number:
                self.add_error('account_number', 'Account number should not be provided for ABS payment type.')

        return cleaned_data # Always return cleaned_data