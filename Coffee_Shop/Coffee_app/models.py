from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.
class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Postre(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Merch(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Asociado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    calificacion = models.IntegerField(validators=[MaxValueValidator(10)])  # Establece el máximo valor de calificación a 10

    def __str__(self):
        return self.nombre

    
class Avatar(models.Model):
    foto = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"  
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    bebidas = models.ManyToManyField(Bebida)
    postres = models.ManyToManyField(Postre)
    merch = models.ManyToManyField(Merch)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'

class BebidaEnCarrito(models.Model):
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_actual = models.DecimalField(max_digits=8, decimal_places=2)

class PostreEnCarrito(models.Model):
    postre = models.ForeignKey(Postre, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_actual = models.DecimalField(max_digits=8, decimal_places=2)

class MerchEnCarrito(models.Model):
    merch = models.ForeignKey(Merch, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_actual = models.DecimalField(max_digits=8, decimal_places=2)