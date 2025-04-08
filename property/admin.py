from django.contrib import admin
from .models import Property  # Ensure you are importing the correct model

admin.site.register(Property)  # Register the model to the admin site
