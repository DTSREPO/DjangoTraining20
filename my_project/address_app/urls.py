from django.urls import path
from .views import districts, district_details

urlpatterns = [
    path('', districts, name='districts'),
    path('<int:id>/', district_details, name='district-id'),
]
