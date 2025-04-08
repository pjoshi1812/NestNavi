

# Create your views here.
from django.shortcuts import render,redirect

from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required,user_passes_test 
from property.models import Property
from home.models import TenantInquiry

@login_required
def owner_dashboard(request):
    # Ensure the user belongs to the "Owners" group
   

    # Get properties and inquiries for the logged-in owner
    properties = Property.objects.filter(owner=request.user)
    inquiries = TenantInquiry.objects.filter(property__owner=request.user)

    return render(request, "owner/dashboard.html", {
        "owner": request.user,
        "properties": properties,
        "inquiries": inquiries,
    })

@login_required
def owner_profile(request):
    if request.user.role != 'owner':
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request, "owner/profile.html", {"owner": request.user})



