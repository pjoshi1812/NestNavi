from django.urls import path
from . import views

app_name = 'property'
urlpatterns = [
    path('detail/', views.detail, name='detail'),  # Detail view
    path('create/', views.property_create, name='property_create'),  # Create property view
    path('list/', views.property_list, name='property_list'), 
     path('toggle_rental_status/<int:property_id>/', views.toggle_rental_status, name='toggle_rental_status'), # List property view
]
