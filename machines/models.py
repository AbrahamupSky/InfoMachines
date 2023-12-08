from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

class Machines(models.Model):
  AREA = (
    ('Acabado Grafico', 'Acabado Grafico'),
    ('Acabado Industrial', 'Acabado Industrial'),
    ('Digital', 'Digital'),
    ('Diseño', 'Diseño'),
    ('Flexo', 'Flexo'),
    ('Gran Formato', 'Gran Formato'),
    ('Offset', 'Offset'),
    ('Talleres', 'Talleres'),
  )

  nombre = models.CharField(max_length=100, null=True, blank=True, unique=True)
  codigo = models.CharField(max_length=50)
  marca = models.CharField(max_length=100)
  modelo = models.CharField(max_length=100)
  noSerie = models.CharField(max_length=100, blank=True)
  equipo = models.CharField(max_length=100, blank=True)
  area = models.CharField(max_length=100, blank=True, choices=AREA)
  responsable = models.CharField(max_length=150, blank=True)
  comentarios = models.TextField(blank=True)
  foto = models.ImageField(upload_to="machines/", null=True, blank=True)
  manual = models.FileField(
    upload_to="manuals/", validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
  )

  def validate_pdf(self, value):
    if not value.name.endswith('.pdf'):
      raise ValidationError('Solo se aceptan archivos PDF')

  def clean(self):
    super().clean()
    self.validate_pdf(self.manual)

  def __str__(self):
    return self.nombre

class Bitacora(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  maquina = models.ForeignKey(Machines, to_field='nombre', on_delete=models.SET_NULL, null=True)
  fecha = models.DateTimeField(default=timezone.now)
  accion = models.CharField(max_length=100)
  tiempo_accion = models.TextField()

  def __str__(self):
    return (f'{self.tiempo_accion} - {self.usuario} - {self.maquina} - {self.accion}')