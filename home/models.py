from django.db import models
from django.conf import settings  # Import settings to use AUTH_USER_MODEL
from property.models import Property

class TenantInquiry(models.Model):
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use AUTH_USER_MODEL for the tenant relationship
        on_delete=models.CASCADE, 
        limit_choices_to={'is_staff': False}
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    inquiry_type = models.CharField(
        max_length=20, 
        choices=[('Book Visit', 'Book Visit'), ('Express Interest', 'Express Interest')]
    )
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant.username} - {self.property.name} - {self.inquiry_type}"
