from django import forms
from .models import Machines

class MachinesForm(forms.ModelForm):
  nombre = forms.CharField(
    label='Nombre',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;'
      }
    ),
  )

  codigo = forms.CharField(
    label='Codigo',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;'
      }
    ),
  )

  marca = forms.CharField(
    label='Marca',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;'
      }
    ),
  )

  modelo = forms.CharField(
    label='Modelo',
    required=True,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;'
      }
    ),
  )

  noSerie = forms.CharField(
    label='Numero de Serie',
    required=False,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;'
      }
    ),
  )

  equipo = forms.CharField(
    label='Equipo',
    required=False,
    widget=forms.TextInput(
      attrs={
        'style': 'font-size: 13px;'
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
        'style': 'font-size: 13px;'
      }
    ),
  )

  comentarios = forms.CharField(
    label='Comentarios',
    required=False,
    widget=forms.Textarea(
      attrs={
        'style': 'font-size: 13px;',
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