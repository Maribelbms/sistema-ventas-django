from django.db import models
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def clean(self):
        if self.precio <= 0:
            raise ValidationError('El precio debe ser mayor que cero.')
        if self.stock < 0:
            raise ValidationError('El stock no puede ser negativo.')

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'Venta {self.id} - {self.cliente}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor que cero.')
        if self.producto.stock < self.cantidad:
            raise ValidationError('No hay suficiente stock para este producto.')

    def __str__(self):
        return f'{self.producto.nombre} x {self.cantidad}'

