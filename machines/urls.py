from django.urls import path
from .views import render_machines, machine_detail, qr

app_name = 'machines'

urlpatterns = [
  path('', render_machines, name='posts'),
  path('<int:machines_id>', machine_detail, name='post_detail'),
]