from django.shortcuts import render, get_object_or_404
from .models import Machines

def render_machines(request):
  posts = Machines.objects.all()
  return render(request, 'machines.html', {'posts': posts})

def machine_detail(request, machines_id):
  post = get_object_or_404(Machines, id=machines_id)
  return render(request, 'machine_detail.html', {'post': post})