from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Articulos

class Articulo(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre



class Proveedor(models.Model):
    NOMBRE_EMPRESA_MAX_LENGTH = 100
    RUT_MAX_LENGTH = 12
    RAZON_SOCIAL_MAX_LENGTH = 100
    PAIS_MAX_LENGTH = 50

    TIPOS_PAGO = [
        ('CR', 'Crédito'),
        ('CO', 'Contado')
    ]

    nombre_empresa = models.CharField(max_length=NOMBRE_EMPRESA_MAX_LENGTH)
    rut = models.CharField(max_length=RUT_MAX_LENGTH, unique=True)
    razon_social = models.CharField(max_length=RAZON_SOCIAL_MAX_LENGTH)
    pais = models.CharField(max_length=PAIS_MAX_LENGTH)
    tipo_pago = models.CharField(max_length=2, choices=TIPOS_PAGO)

    def __str__(self):
        return self.nombre_empresa

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    procedencia = models.CharField(max_length=100)
    codigo = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"


class Articulo(models.Model):
    sku = models.CharField(max_length=50, primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nom_region = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_region

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_comuna

class Cliente(models.Model):
    rut_cli = models.CharField(max_length=20, primary_key=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class CategoriaPolera(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_cat = models.CharField(max_length=30)

class Producto(models.Model):
    id_productos = models.IntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=30)
    descrip_produc = models.CharField(max_length=40)
    precio_produc = models.DecimalField(max_digits=20, decimal_places=2)
    stock_produc = models.IntegerField()
    categoria = models.ForeignKey(CategoriaPolera, on_delete=models.CASCADE)

class DetallePedido(models.Model):
    id_detalle = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    categoria_polera = models.ForeignKey(CategoriaPolera, on_delete=models.CASCADE)

class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    total_pedi = models.DecimalField(max_digits=20, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalle_pedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE)


class Contacto(models.Model):
    correo = models.EmailField(max_length=100)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    consulta = models.TextField()

    def __str__(self):
        return self.nombre_completo
    
class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.genero

class Alumno(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE) 
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title