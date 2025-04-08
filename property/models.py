from django.db import models

# Create your models here.
from django.db import models
from userauth.models import User

class Property(models.Model):
    # The ForeignKey establishes a relationship with the User model
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'owner'})
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    rent_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField(help_text="Comma-separated amenities like WiFi, AC, Laundry")
    available_rooms = models.IntegerField()
    is_rented = models.BooleanField(default=False, help_text="Indicates whether the property is rented")
    property_photo = models.ImageField(upload_to='property_photos/', null=True, blank=True)



    def __str__(self):
        return self.address
