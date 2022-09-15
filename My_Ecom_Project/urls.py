from django.contrib import admin
from django.urls import path, include

# TO show media files
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Shop.urls')),
    path('account/', include('App_Login.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, decument_root=settings.MEDIA_ROOT)



