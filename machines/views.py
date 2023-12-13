from .models import Machines, Bitacora
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import MachinesForm, BitacoraForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404

def render_machines(request):
  posts = Machines.objects.all()
  return render(request, 'machines/machines.html', {'posts': posts})

def machine_detail(request, machines_id):
  post = get_object_or_404(Machines, id=machines_id)
  return render(request, 'machines/machine_detail.html', {'post': post})

@login_required(login_url='/login/')
def add_machine(request):
  if request.method == 'POST':
    form = MachinesForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, 'La maquina fue agregada con exito')
      return HttpResponseRedirect('machines/add_machine')

    else:
      print(form.errors)
      return render(request, 'machines/addMachine.html', {'form': form})

  else:
    form = MachinesForm()
    return render(request, 'machines/addMachine.html', {'form': form})

@login_required(login_url='/login/')
def add_bitacora(request):
  if request.method == 'POST':
    form = BitacoraForm(request.POST, request.FILES)
    if form.is_valid():
      maquina_id = form.cleaned_data['maquina'].id

      if Machines.objects.filter(id=maquina_id).exists():
        form.save()
        messages.success(request, 'La bitácora fue agregada con éxito')
        return redirect('home')
      else:
        messages.error(request, 'La máquina seleccionada no existe.')
        return render(request, 'logbook/addBitacora.html', {'form': form})
    else:
      print(form.errors)
      return render(request, 'logbook/addBitacora.html', {'form': form})
  else:
    form = BitacoraForm()
    return render(request, 'logbook/addBitacora.html', {'form': form})
  
@login_required
def table_bitacora(request):
  posts = Bitacora.objects.all()
  return render(request, 'logbook/tableBitacora.html', {'posts': posts})

@login_required
def view_bitacora(request, bitacora_id):
  bitacora = get_object_or_404(Bitacora, id=bitacora_id)
  return render(request, 'logbook/viewBitacora.html', {'bitacora': bitacora})

def login_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Sesión iniciada con exito')
      return redirect('home')

    else:
      messages.error(request, 'Credenciales incorrectas')
      return redirect('login')

  else:
    return render(request, 'auth/login.html')

@login_required(login_url='/login/')
def logout_user(request):
  logout(request)
  messages.success(request, 'Sesión cerrada con exito')
  return redirect('login')

@login_required(login_url='/login/')
def home(request):
  return render(request, 'home.html')