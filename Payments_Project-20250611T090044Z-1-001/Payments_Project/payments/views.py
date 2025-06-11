from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse # Import JsonResponse
from .models import PaymentType
from .forms import PaymentTypeForm
from django.template.loader import render_to_string # Import to render partial templates

# No change needed for payment_type_list as it's the main page now.
def payment_type_list(request):
    payment_types = PaymentType.objects.all()
    return render(request, 'payments/payment_type_list.html', {'payment_types': payment_types})

# NEW: View to return just the table rows for AJAX update
def payment_type_list_partial(request):
    payment_types = PaymentType.objects.all()
    return render(request, 'payments/_payment_type_table_rows.html', {'payment_types': payment_types})

# NEW: View to return the Add form HTML for the modal
def add_payment_type_modal(request):
    form = PaymentTypeForm()
    return render(request, 'payments/payment_type_form.html', {'form': form})

# Modify add_payment_type to handle AJAX submissions from modal
def add_payment_type(request): # This now handles the POST from the modal
    if request.method == 'POST':
        form = PaymentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Payment type added successfully!'})
        else:
            # If form is not valid, render the form again with errors
            form_html = render_to_string('payments/payment_type_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'form_html': form_html})
    # This view is now only for POST requests from the modal,
    # or it can return a 405 Method Not Allowed if accessed via GET
    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)


# NEW: View to return the View/Detail content for the modal
def view_payment_type_modal(request, pk):
    payment_type = get_object_or_404(PaymentType, pk=pk)
    return render(request, 'payments/_payment_type_detail_content.html', {'payment_type': payment_type})


# NEW: View to return the Edit form HTML for the modal
def edit_payment_type_modal(request, pk):
    payment_type = get_object_or_404(PaymentType, pk=pk)
    form = PaymentTypeForm(instance=payment_type)
    return render(request, 'payments/payment_type_form.html', {'form': form})

# Modify edit_payment_type to handle AJAX submissions from modal
def edit_payment_type(request, pk): # This now handles the POST from the modal
    payment_type = get_object_or_404(PaymentType, pk=pk)
    if request.method == 'POST':
        form = PaymentTypeForm(request.POST, instance=payment_type)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Payment type updated successfully!'})
        else:
            form_html = render_to_string('payments/payment_type_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'form_html': form_html})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)


# Modify delete_payment_type to handle AJAX submissions from modal
def delete_payment_type(request, pk): # This now handles the POST from the modal
    payment_type = get_object_or_404(PaymentType, pk=pk)
    if request.method == 'POST':
        payment_type_name = payment_type.payment_type # Get name before deleting
        payment_type.delete()
        return JsonResponse({'success': True, 'payment_type_name': payment_type_name})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)