from django.test import TestCase
from .models import Cliente, Producto

class ClienteTestCase(TestCase):
    def setUp(self):
        Cliente.objects.create(nombre="Cliente1", email="cliente1@example.com")

    def test_cliente_nombre(self):
        cliente = Cliente.objects.get(nombre="Cliente1")
        self.assertEqual(cliente.nombre, "Cliente1")

class ProductoTestCase(TestCase):
    def setUp(self):
        Producto.objects.create(nombre="Producto1", precio=10, stock=5)

    def test_producto_precio(self):
        producto = Producto.objects.get(nombre="Producto1")
        self.assertEqual(producto.precio, 10)
