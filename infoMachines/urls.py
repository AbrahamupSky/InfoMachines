from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from machines import urls
from django.contrib.auth.decorators import login_required
from machines.views import render_machines, machine_detail, add_machine, login_user, logout_user

from viewMachines import views

urlpatterns = [
  path('jet/', include('jet.urls', 'jet')),
  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

  path('<int:machines_id>', machine_detail, name='post_detail'),
  path('add_machine/', login_required(add_machine), name='add_machine'),
  path('machines/', render_machines, name='posts'),

  path('login/', login_user, name='login'),
  path('logout/', logout_user, name='logout'),

  path('admin/', admin.site.urls),
  path('', views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)