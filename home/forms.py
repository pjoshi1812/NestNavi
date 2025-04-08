from django import forms
from .models import TenantInquiry

class TenantInquiryForm(forms.ModelForm):
    class Meta:
        model = TenantInquiry
        fields = ['inquiry_type', 'message']
        widgets = {
            'inquiry_type': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
