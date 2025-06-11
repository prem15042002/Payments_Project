from django.urls import path
from . import views

urlpatterns = [
    # Main list page (remains the same as it's the SPA entry point)
    path('', views.payment_type_list, name='payment_type_list'),

    # NEW: Endpoint for partial table update (AJAX)
    path('list/partial/', views.payment_type_list_partial, name='payment_type_list_partial'),

    # NEW: Endpoint to get the Add form HTML for the modal (GET request)
    path('add/modal/', views.add_payment_type_modal, name='add_payment_type_modal'),
    # Original add view, now handling POST from modal (AJAX)
    path('add/', views.add_payment_type, name='add_payment_type'), # Keep original name

    # NEW: Endpoint to get the View/Detail HTML for the modal (GET request)
    path('view/modal/<int:pk>/', views.view_payment_type_modal, name='view_payment_type_modal'),
    # No direct view page, as it's now a modal. Original 'view_payment_type' removed or repurposed.
    # path('view/<int:pk>/', views.view_payment_type, name='view_payment_type'), # <-- This direct view is no longer used for navigation

    # NEW: Endpoint to get the Edit form HTML for the modal (GET request)
    path('edit/modal/<int:pk>/', views.edit_payment_type_modal, name='edit_payment_type_modal'),
    # Original edit view, now handling POST from modal (AJAX)
    path('edit/<int:pk>/', views.edit_payment_type, name='edit_payment_type'), # Keep original name

    # Original delete view, now handling POST from modal (AJAX)
    path('delete/<int:pk>/', views.delete_payment_type, name='delete_payment_type_modal'), # Renamed for clarity
]