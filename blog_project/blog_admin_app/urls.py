from django.urls import path
from .views import dashboard, author_list, create_author, category_list, create_category, post_list, create_post

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('author/', author_list, name='author-list'),
    path('create-author/', create_author, name='create-author'),
    path('category/', category_list, name='category-list'),
    path('create-category/', create_category, name='create-category'),
    path('post/', post_list, name='post-list'),
    path('create-post/', create_post, name='create-post'),
]
