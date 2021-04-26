from django.db import models
from django.utils import timezone

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la categoría')
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name= 'Marca'
        verbose_name_plural= 'Marcas'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100 ,verbose_name='Nombre')
    price = models.IntegerField(verbose_name='Precio')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Marca')
    state = models.BooleanField(verbose_name='¿Es Nuevo?')
    manufacturing = models.DateTimeField(verbose_name='Fecha de fabricacion', default= timezone.now )
    image = models.ImageField(verbose_name='Imagen', upload_to='products', blank=True, null=True)
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'

    def __str__(self):
        return self.name