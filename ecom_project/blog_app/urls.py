from django.urls import path
from django.conf import settings
from .views import home, post_list, post_details, post_list_by_author, about, contact


urlpatterns = [
    path('', home, name='home'),
    path('blog/', post_list, name='post-list'),
    path('blog/post/<int:post_id>', post_details, name='post-details'),
    path('blog/post/<str:author>', post_list_by_author, name='author-post'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
