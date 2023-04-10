from django.db import models

# Create your models here.

class Dpi(models.Model):
    sexo_choices = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')

    ]

    noDpi = models.IntegerField(verbose_name='Numero de DPI')
    fecha_nac = models.DateField(verbose_name='Fecha Nacimiento')
    lugar_nac = models.CharField(max_length=100, verbose_name='Lugar de nacimiento')
    municipio = models.CharField(max_length=50, verbose_name='Municipio')
    departamento = models.CharField(max_length=50, verbose_name='Departamento')
    nacionalidad = models.CharField(max_length=50, verbose_name='Nacionalidad')
    fecha_emision = models.DateField(verbose_name='Fecha de emision de DPI')
    fecha_venc = models.DateField(verbose_name='Fecha de Vencimiento')
    sexo = models.CharField(max_length=12, choices=sexo_choices, verbose_name='Genero')


    def __str__(self):
        return str(self.noDpi) + '-' + str(self.fecha_nac)

    class Meta:
        verbose_name = 'DPi'
        verbose_name_plural = 'DPIS'
        ordering = ['id']


class Persona(models.Model):
    religion_choices = [
        ('Niguno', 'Ninguno'),
        ('Catalogo', 'Catolico'),
        ('Evangelico', 'Evangelico'),
        ('Mornon', 'Mormon'),
        ('Ateo', 'Ateo')
    ]

    pnombre = models.CharField(max_length=100, verbose_name='Primer Nombre')
    snombre = models.CharField(max_length=100, verbose_name='Segundo Nombre')
    papellido = models.CharField(max_length=50, verbose_name='Primer Apellido')
    sapellido = models.CharField(max_length=50, verbose_name='Segundo Apellido')
    dpi = models.ForeignKey(Dpi, on_delete=models.CASCADE, verbose_name='Numero de DPI')
    nit = models.CharField(max_length=15, verbose_name='Numero de Nit')
    direccion = models.CharField(max_length=100, verbose_name='Direccion Actual')
    aldea = models.CharField(max_length=50, verbose_name='Aldea')
    municipio = models.CharField(max_length=50, verbose_name='Municipio')
    departamento = models.CharField(max_length=50, verbose_name='Departamento')
    email = models.EmailField(verbose_name='Correo electronico')
    telefono = models.IntegerField(verbose_name='Numero de telefono')
    religion = models.CharField(max_length=11, choices=religion_choices, verbose_name='Religion')

    def __str__(self):

        return self.pnombre + ' ' + self.papellido
    

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']
    

