from django.urls import path
from .views import students, student_details


urlpatterns = [
    path('list/', students, name='std-list'),
    path('<int:id>/', student_details, name='std-id'),
]
