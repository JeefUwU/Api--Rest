from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Producto
from datetime import date

                                #Unitaria = Funciona
class ProductoTestCase(TestCase):
    def setUp(self):
        Producto.objects.create(
            codigo_producto="prueba1",
            marca="prueba1",
            codigo="abc123",
            nombre="prueba1",
            precio=99999,
            fecha=date(2002, 10, 15)
        )
        Producto.objects.create(
            codigo_producto="prueba 2",
            marca="prueba 2",
            codigo="xyz456",
            nombre="prueba 2",
            precio=99999,
            fecha=date(2002, 11, 10)
        )

    def test_producto_creation(self):
        producto1 = Producto.objects.get(nombre="prueba1")
        producto2 = Producto.objects.get(nombre="prueba 2")

                                #Integrales = No Funciona
class productoTests(APITestCase):
    
    def setUp(self):
        self.producto1 = Producto.objects.create(
            codigo_producto='prod1',
            marca='marca1',
            codigo='001',
            nombre='prueba1',
            precio=1000,
            fecha='2024-06-16',
        )
        self.producto2 = Producto.objects.create(
            codigo_producto='prod2',
            marca='marca2',
            codigo='002',
            nombre='prueba2',
            precio=2000,
            fecha='2024-06-17',
        )

    def test_producto_list(self):
        url = reverse('producto-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_producto_detail(self):
        url = reverse('producto-detail', args=[self.producto1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'prueba1')

    def test_producto_create(self):
        # Definir la URL a la que se enviará la solicitud POST
        url = reverse('producto-list')  # Ajusta 'producto-list' según tu configuración de URL

        # Datos a enviar en la solicitud POST para crear un nuevo producto
        data = {
            'codigo_producto': 'nuevo_producto',
            'marca': 'marca_nueva',
            'codigo': 'new123',
            'nombre': 'Nuevo Producto',
            'precio': 9999,
            'fecha': '2024-06-16',
        }

        # Enviar la solicitud POST y capturar la respuesta
        response = self.client.post(url, data, format='json')
    
        try:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        except AssertionError:
            print(response.data)  # Muestra los datos de la respuesta para entender el error
            raise  # Re-lanza la excepción para que la prueba falle explícitamente si hay un error

        # Verificar que se haya creado un nuevo producto en la base de datos
        self.assertEqual(Producto.objects.count(), 3)  # Asegúrate de ajustar este valor según corresponda
        self.assertEqual(Producto.objects.last().nombre, 'Nuevo Producto')