# products/admin.py

from django.contrib import admin
from .models import Product # Import the Product model

# Register your models here.
admin.site.register(Product) # Tell the admin to manage Products