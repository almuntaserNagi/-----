from django.contrib import admin
from django.urls import path, include
from mirror.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mirror.urls')),
    
    # path("", create_customer_and_assets, name='homy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)