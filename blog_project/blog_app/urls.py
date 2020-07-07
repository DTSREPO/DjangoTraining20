from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about, contact


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
