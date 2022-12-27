from django.db import models
from datetime import datetime ,date



# Create your models here.

class Prof(models.Model):
    nombre = models.CharField(max_length=200,verbose_name= 'nombre', default='')
    apellido = models.CharField(max_length=200,verbose_name= 'apellido', default='')
    email = models.EmailField(max_length=200, verbose_name= 'email', default='')
    id = models.AutoField(primary_key=True, verbose_name= 'id_profesional')
    telefono = models.CharField(max_length=200,verbose_name= 'telefono', default='')
    ocupacion = models.CharField(max_length=200,verbose_name= 'ocupacion', default='')

    class Meta:
        ordering = ['nombre']


    def __str__(self):
        fila = self.nombre + " " + self.apellido + " / " + self.ocupacion
        return fila

diab_status = [
    ['SI','Si'],
    ['NO','No'],
]

horarios = [
    ['10:00 a 10:30','10:00 a 10:30'],
    ['10:30 a 11:00','10:30 a 11:00'],
    ['11:00 a 11:30','11:00 a 11:30'],
    ['11:30 a 12:00','11:30 a 12:00'],
    ['12:00 a 12:30','12:00 a 12:30'],
    ['12:30 a 01:00','12:30 a 01:00'],
    ['01:00 a 01:30','01:00 a 01:30'],
    ['01:30 a 02:00','01:30 a 02:00'],
    ['02:00 a 02:30','02:00 a 02:30'],
    ['02:30 a 03:00','02:30 a 03:00'],
    ['03:00 a 03:30','03:00 a 03:30'],
    ['03:30 a 04:00','03:30 a 04:00'],
    ['04:00 a 04:30','04:00 a 04:30'],
    ['04:30 a 05:00','04:30 a 05:00'],
    ['05:00 a 05:30','05:00 a 05:30'],
    ['05:30 a 06:00','05:30 a 06:00'],
    ['06:00 a 06:30','06:00 a 06:30'],
    ['06:30 a 07:00','06:30 a 07:00'],
    
]

dias_lab = [
    ['Lunes','Lunes'],
    ['Martes','Martes'],
    ['Miercoles','Miercoles'],
    ['Jueves','Jueves'],
    ['Viernes','Viernes'],
    ['Sabado','Sabado'],
]

class Cliente(models.Model):
    nombre = models.CharField(max_length=200,verbose_name= 'nombre', default='')
    apellido = models.CharField(max_length=200,verbose_name= 'apellido', default='')
    email = models.EmailField(max_length=200,verbose_name= 'email')
    rut = models.CharField(max_length=10,primary_key=True, null=False,verbose_name= 'rut', default='')
    telefono = models.CharField(max_length=200,verbose_name= 'telefono', default='')
    ficha = models.TextField(null =True, verbose_name= 'ficha')
    diab = models.CharField(max_length=2,choices=diab_status, default='----')



    class Meta:
        ordering = ['nombre']

    def __str__(self):
        fila = "Nombre: " + self.nombre + " " + self.apellido + "    /    Rut: " + self.rut
        return fila


class Atencion(models.Model):
    id_prof = models.ForeignKey(Prof,on_delete=models.CASCADE, verbose_name='Atención')
    nombre = models.CharField(max_length=200,verbose_name= 'Nombre', default='')
    apellido = models.CharField(max_length=200,verbose_name= 'Apellido', default='')
    email = models.EmailField(max_length=200,verbose_name= 'Email', default='')
    rut = models.CharField(max_length=10,null=False,verbose_name= 'Rut', default='')
    telefono = models.CharField(max_length=200,verbose_name= 'Telefono', default='')
    diab = models.CharField(max_length=2,choices=diab_status, default='----')
    fecha= models.DateField(auto_now=False, verbose_name='fecha')
    hora = models.CharField(max_length=200,choices=horarios, default='----')
    coment = models.TextField(null =True, verbose_name= 'Comentarios', default='')
    

    def __str__(self):
        return self.nombre + " " + self.apellido 