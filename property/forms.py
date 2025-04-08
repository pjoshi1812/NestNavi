# forms.py (in property app)
from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'city', 'state', 'pincode', 'rent_per_month', 'amenities', 'available_rooms','is_rented','property_photo']
