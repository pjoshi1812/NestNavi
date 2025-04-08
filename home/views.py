from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from property.models import Property
from django.http import HttpResponseForbidden
# from .forms import PropertyForm

from .models import Property, TenantInquiry
from django.contrib.auth.decorators import login_required,user_passes_test 
from property.models import Property
from home.models import TenantInquiry


# Create your views here.

def index(request):
    properties = Property.objects.all()  # Fetch all properties
    return render(request,'home/index.html', {'properties': properties})

def details(request, pk):
    # Fetch the property by primary key, ensuring it is not rented
    property_obj = get_object_or_404(Property, pk=pk)

    # Redirect or deny access if the property is rented
    if property_obj.is_rented:
        return HttpResponseForbidden("This property is no longer available.")  # Or redirect to another page

    return render(request, 'home/detail.html', {'property': property_obj})


@login_required
@user_passes_test(lambda u: not u.is_staff, login_url='/')  # Only tenants can express interest
def inquiry(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)

    # Create a new inquiry for the tenant
    TenantInquiry.objects.create(
        tenant=request.user,
        property=property_obj,
        inquiry_type="Express Interest",
        message="Tenant has expressed interest in this property."
    )

    return render(request, 'home/inquiry_success.html', {'property': property_obj})

# View to list inquiries (restricted to owners or admins)
@login_required
@user_passes_test(lambda u: u.is_staff or u.groups.filter(name='Owners').exists())
def inquiries_list(request):
    inquiries = TenantInquiry.objects.all().select_related('tenant', 'property')
    return render(request, 'home/inquiries_list.html', {'inquiries': inquiries})