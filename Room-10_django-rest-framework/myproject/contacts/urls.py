from django.urls import path
from .views import contact_list

urlpatterns = [
    path('api/', contact_list)
]