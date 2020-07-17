from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Category
from blog.serializers import CategorySerializer

CATEGORY_URL = reverse('blog:category-list')


class PublicCategoryApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_category_invalid(self):
        payload = {'name': ''}
        res = self.client.post(CATEGORY_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_category(self):
        payload = {
            'name': 'Food'
        }
        res = self.client.post(CATEGORY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_retrieve_categories(self):
        Category.objects.create(name='Food')
        Category.objects.create(name='Technology')

        res = self.client.get(CATEGORY_URL)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
