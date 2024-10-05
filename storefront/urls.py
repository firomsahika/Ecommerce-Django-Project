from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

# from playground.views import index, contact

urlpatterns = [
    path('', include('playground.urls')),
    path('admin/', admin.site.urls),
    # path('items/', include('item.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

