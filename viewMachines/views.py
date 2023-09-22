from django.shortcuts import render
from .models import MachinePost

def home(request):
  machines = MachinePost.objects.all()
  return render(request, 'home.html', {'machines': machines})