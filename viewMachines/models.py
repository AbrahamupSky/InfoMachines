from django.db import models

from django.db import models
import datetime

class MachinePost(models.Model):
  DEPARTMENT = (
    ('Acabado Grafico', 'Acabado Grafico'),
    ('Acabado Industrial', 'Acabado Industrial'),
    ('Gran Formato', 'Gran Formato'),
    ('Impresión', 'Impresión'),
    ('Prensas', 'Prensas'),
    ('Prensa', 'Prensa'),
  )

  AREA = (
    ('Digital', 'Digital'),
    ('Diseño', 'Diseño'),
    ('Flexo', 'Flexo'),
    ('Gran Formato', 'Gran Formato'),
    ('Offset', 'Offset'),
    ('Talleres', 'Talleres'),
  )

  brand = models.CharField(max_length=100, blank = True)
  department = models.CharField(max_length=100, blank = True, choices=DEPARTMENT)
  area = models.CharField(max_length=100, blank = True, choices=AREA)
  responsible = models.CharField(max_length=150, blank = True)
  date = models.DateField(datetime.date.today)