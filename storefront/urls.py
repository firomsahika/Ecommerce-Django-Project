from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),

    path('admin/', admin.site.urls),
    # path('items/', include('item.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

