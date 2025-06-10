from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported here

urlpatterns = [
    path('admin/', admin.site.urls), # This is for Django's built-in admin
    path('payments/', include('payments.urls')), # This routes /payments/ to your app's URLs
    path('', include('payments.urls')), # OPTIONAL: This makes your app's list page the homepage
]