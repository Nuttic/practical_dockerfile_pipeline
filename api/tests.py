from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Cat


class CatAPITests(APITestCase):
    def setUp(self):
        self.cat = Cat.objects.create(name="Барсик", breed="Британский", age=3, is_cute=True)

    def test_health_check(self):
        url = reverse('health-check')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')
        self.assertEqual(response.data['service'], 'koticback')
        self.assertEqual(response.data['cats_count'], 1)

    def test_list_cats(self):
        url = reverse('cat-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], 'Барсик')

    def test_create_cat(self):
        url = reverse('cat-list')
        data = {
            'name': 'Мурка',
            'breed': 'Сиамская',
            'age': 2,
            'is_cute': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cat.objects.count(), 2)
        self.assertEqual(response.data['name'], 'Мурка')

    def test_random_cat(self):
        url = reverse('cat-random')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Барсик')
