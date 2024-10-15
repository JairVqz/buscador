from django.db import models

# Create your models here.

from django.db import models

class Beneficiario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    programa = models.CharField(max_length=100)
    area_programa = models.CharField(max_length=100)
    ejercicio = models.IntegerField(max_length=4)
    fecha = models.DateField()
    municipio = models.CharField(max_length=255)

    class Meta:
        db_table = 'beneficiarios'  # Nombre que tendra la tabla en la base de datos

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    prefijo = models.CharField(max_length=10)
    nombre_completo = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'areas'  # Nombre que tendra la tabla en la base de datos

class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    cve_mpio = models.CharField(max_length=10)
    cve_mpio_full = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    territorio = models.IntegerField(max_length=100)
    
    class Meta:
        db_table = 'municipios'  # Nombre que tendra la tabla en la base de datos