from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required

def detail(request):
    if not request.user.is_authenticated:
        return redirect('userauth:sign-in')  # Replace 'userauth:login' with your actual login URL
    
    # Your code for booking the visit
    # Fetch the property, process the visit, etc.
    return render(request, 'property/detail.html')





def property_list(request):
    properties = Property.objects.all()  # Fetch all properties
    return render(request, 'property/property_list.html', {'properties': properties})

# Property Create view
@login_required
def property_create(request):
    if request.user.role != 'owner':  # Check if the logged-in user is an owner
        return redirect('home')  # Redirect to home page if not an owner
    
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)  # Pass request.FILES to handle file upload
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user  # Set the logged-in user as the property owner
            property.save()
            return redirect('property:property_list')  # Redirect to property list after saving
    else:
        form = PropertyForm()
    
    return render(request, 'property/property_form.html', {'form': form})

@login_required
def toggle_rental_status(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    # Toggle the is_rented status
    property.is_rented = not property.is_rented
    property.save()
    return redirect('property:property_list') 