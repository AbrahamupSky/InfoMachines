from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from machines import urls

from viewMachines import views

urlpatterns = [
  path('jet/', include('jet.urls', 'jet')),
  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),


  path('machines/admin/', admin.site.urls),
  path('', views.home, name='home'),
  path('machines/', include(urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)