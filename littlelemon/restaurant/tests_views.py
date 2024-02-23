from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from . import serializers
from . import models

class MenuViewTest(TestCase):
  def setUp(self):
    models.Menu.objects.create(title='Spagetti', price=9.99, inventory=2)
    models.Menu.objects.create(title='Tea', price=3.40, inventory=10)
    models.Menu.objects.create(title='Coffee', price=6.99, inventory=4)

  def test_getall(self):
    client = APIClient()
    response = client.get(reverse('menu-items'))
    serialized_data = serializers.MenuSerializer(models.Menu.objects.all(), many=True).data
    self.assertEqual(response.data, serialized_data)