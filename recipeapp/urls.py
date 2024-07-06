from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the view for the root URL
]
