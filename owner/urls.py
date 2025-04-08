# owner/urls.py
from django.urls import path
from owner import views
from home import views as hviews

app_name = 'owner'  # Correctly set the namespace for the owner app

urlpatterns = [
    path('dashboard/', views.owner_dashboard, name='dashboard'),
    path('profile/', views.owner_profile, name='profile'),

    
]
