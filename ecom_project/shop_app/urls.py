from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, product_dtl, category_product, product_filter_price, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pid>', product_dtl, name='product_dtl'),
    path('category/<str:category>', category_product, name='category_product'),
    path('price/<int:price>', product_filter_price, name='price_range'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
