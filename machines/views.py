from .models import Machines
from .forms import MachinesForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout

def render_machines(request):
  posts = Machines.objects.all()
  return render(request, 'machines.html', {'posts': posts})

def machine_detail(request, machines_id):
  post = get_object_or_404(Machines, id=machines_id)
  return render(request, 'machine_detail.html', {'post': post})

def add_machine(request):
  if request.method == 'POST':
    form = MachinesForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, 'La maquina fue agregada con exito')
      return HttpResponseRedirect('/add_machine')

    else:
      print(form.errors)
      return render(request, 'addMachine.html', {'form': form})

  else:
    form = MachinesForm()
    return render(request, 'addMachine.html', {'form': form})
  
def login_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')

    else:
      messages.success(request, 'Credenciales incorrectas')
      return redirect('login')

  else:
    return render(request, 'auth/login.html')

def logout_user(request):
  logout(request)
  messages.success(request, 'Sesión cerrada con exito')
  return redirect('login')

def qr(request):
  return render(request, 'qr.html')