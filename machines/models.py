from django.db import models

class Machines(models.Model):
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

  code = models.CharField(max_length=50)
  brand = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  noSerie = models.CharField(max_length=100, blank = True)
  equip = models.CharField(max_length=100, blank = True)
  department = models.CharField(max_length=100, blank = True, choices=DEPARTMENT)
  area = models.CharField(max_length=100, blank = True, choices=AREA)
  responsible = models.CharField(max_length=150, blank = True)
  comments = models.TextField(blank = True)

  manual = models.FileField(upload_to="manuals/")