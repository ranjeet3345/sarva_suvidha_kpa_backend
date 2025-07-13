from django.urls import path
from . import views

urlpatterns = [
    path('api/forms/wheel-specifications', views.submit_wheel_specification, name='submit_wheel_specification'),
    path('api/forms/wheel-specifications/', views.get_wheel_specifications, name='get_wheel_specifications'),
]
