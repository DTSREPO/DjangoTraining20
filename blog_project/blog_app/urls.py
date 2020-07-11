from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pid>', single_post, name='single_post'),
    path('author/<str:author>', author_post, name='author_post'),
    path('category/<str:category>', category_post, name='category_post'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('search/', search_post, name='search_post')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
