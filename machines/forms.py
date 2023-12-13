from django import forms
from .models import Machines, Bitacora

class MachinesForm(forms.ModelForm):
  nombre = forms.CharField(
    label='Nombre',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Nombre de la maquina'
      }
    ),
  )

  codigo = forms.CharField(
    label='Codigo',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Codigo de la maquina'
      }
    ),
  )

  marca = forms.CharField(
    label='Marca',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Marca de la maquina'
      }
    ),
  )

  modelo = forms.CharField(
    label='Modelo',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Modelo de la maquina'
      }
    ),
  )

  noSerie = forms.CharField(
    label='Numero de Serie',
    required=False,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Numero de serie de la maquina'
      }
    ),
  )

  equipo = forms.CharField(
    label='Equipo',
    required=False,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Equipo de la maquina'
      }
    ),
  )

  area = forms.ChoiceField(
    label='Area',
    required=True,
    choices=Machines.AREA,
    widget=forms.Select(
      attrs={
        'style': 'font-size: 13px;'
      }
    ),
  )

  responsable = forms.CharField(
    label='Responsable',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Responsable de la maquina'
      }
    ),
  )

  comentarios = forms.CharField(
    label='Comentarios',
    required=False,
    widget=forms.Textarea(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Comentarios de la maquina',
        'rows': 3
      }
    ),
  )

  foto = forms.ImageField(
    label='Fotografia',
    required=True,
    widget=forms.ClearableFileInput(
      attrs={
        'style': 'font-size: 13px;',
        'accept': 'image/png, image/jpeg'
      }
    ),
  )

  manual = forms.FileField(
    label='Manual',
    required=True,
    widget=forms.ClearableFileInput(
      attrs={
        'style': 'font-size: 13px;',
        'accept': 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document'
      }
    ),
    error_messages={
      'required': 'La contasancia de situación fiscal es requerida',
      'accept': 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    },
  )

  class Meta:
    model = Machines
    fields = '__all__'

class BitacoraForm(forms.ModelForm):
  maquina = forms.ModelChoiceField(
    queryset=Machines.objects.all(),
    label='Maquina',
    widget=forms.Select(attrs={'style': 'font-size: 13px;'}),
    required=True,
  )

  fecha = forms.DateField(
    label='Fecha',
    required=True,
    widget=forms.DateInput(
      attrs={
        'type': 'date',
        'style': 'font-size: 13px;'
      }
    ),
  )

  accion = forms.CharField(
    label='Accion',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;',
        'placeholder': 'Acciones realizadas en la maquina'
      }
    ),
  )

  tiempo_accion = forms.CharField(
    label='Comentarios',
    required=False,
    widget=forms.Textarea(
      attrs={
        'style': 'font-size: 13px;',
        'rows': 3,
        'placeholder': 'Comentarios adicionales'
      }
    ),
  )

  file = forms.FileField(
    label='Fotografia de la bitacora fisica',
    required=True,
    widget=forms.ClearableFileInput(
      attrs={
        'style': 'font-size: 13px;',
        'accept': 'image/png, image/jpeg'
      }
    ),
  )

  class Meta:
    model = Bitacora
    fields = ['maquina', 'fecha', 'accion', 'tiempo_accion', 'file']