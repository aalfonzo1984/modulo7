from django.db import models
from django.core.validators import MinValueValidator
from datetime import date



class Laboratorio(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre del laboratorio')
    ciudad = models.CharField(max_length=150, verbose_name='Ciudad')
    pais = models.CharField(max_length=50, verbose_name='País')
    
    
    class Meta:
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'
        ordering = ['id']
        
    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre Director General')
    especialidad = models.CharField(max_length=100, verbose_name='Especialidad')
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Director General'
        verbose_name_plural = 'Directores Generales'
        ordering = ['id']
        
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre Producto')
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[MinValueValidator(date(2015,1,1))], verbose_name='Fecha Fabricación')
    p_costo = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Precio Costo')
    p_venta = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Precio Venta')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
        
    