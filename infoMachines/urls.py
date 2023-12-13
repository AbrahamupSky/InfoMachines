from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from machines.views import render_machines, machine_detail, add_machine, login_user, logout_user, add_bitacora, home, table_bitacora, view_bitacora

urlpatterns = [
  # ? ---- Panel de Administracion ----
  path('admin/', admin.site.urls),
  path('jet/', include('jet.urls', 'jet')),
  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

  # ? ---- Maquinas ----
  path('<int:machines_id>', machine_detail, name='post_detail'),
  path('add_machine/', add_machine, name='add_machine'),
  path('machines/', render_machines, name='posts'),

  # ? ---- Bitacora ----
  path('bitacora/', add_bitacora, name='add_bitacora'),
  path('add_bitacora/', table_bitacora, name='bitacoras'),
  path('view_bitacora/<int:bitacora_id>/', view_bitacora, name='view_bitacora'),

  # ? ---- Auth ----
  path('login/', login_user, name='login'),
  path('logout/', logout_user, name='logout'),

  path('', home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)