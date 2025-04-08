from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    # Existing routes
    path('', views.index, name='index'),
    path('home/<int:pk>/', views.details, name='detail'),
    
    # Routes for tenant inquiries
    path('inquiry/<int:property_id>/', views.inquiry, name='inquiry'),  # Tenant submits inquiry
    path('inquiries/', views.inquiries_list, name='inquiries_list'),   # List all inquiries (owners/admins)
 
    
]
