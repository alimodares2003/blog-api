from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Post, Category
from blog.serializers import PostSerializer

POST_URL = reverse('blog:post-list')


def detail_url(category_id):
    return reverse('blog:post-detail', args=[category_id])


class PublicPostApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_post(self):
        category = Category.objects.create(name='Test')
        payload = {
            'title': 'Test Title',
            'content': 'test content',
            'category_id': category.id,
        }
        res = self.client.post(POST_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_retrieve_posts(self):
        category1 = Category.objects.create(name='Test1')
        Post.objects.create(title='Test1', content='test content', category_id=category1)

        category2 = Category.objects.create(name='Test2')
        Post.objects.create(title='Test2', content='test content', category_id=category2)

        res = self.client.get(POST_URL)

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_detail_post(self):
        category = Category.objects.create(name='Technology')
        post = Post.objects.create(title='Python', content='test content', category_id=category)

        url = detail_url(post.id)
        res = self.client.get(url)
        serializer = PostSerializer(post)
        self.assertEqual(res.data, serializer.data)

    def test_partial_update_post(self):
        category = Category.objects.create(name='Technology')
        post = Post.objects.create(title='Python Presentation', content='test content', category_id=category)

        payload = {'title': 'Python Presentation', 'content': 'test presentation', 'category_id': category.id}
        url = detail_url(post.id)
        self.client.patch(url, payload)

        post.refresh_from_db()
        self.assertEqual(post.title, payload['title'])

    def test_full_update_post(self):
        category = Category.objects.create(name='Technology')
        post = Post.objects.create(title='Python Presentation', content='test content', category_id=category)

        payload = {'title': 'Kotlin Presentation', 'content': 'test presentation', 'category_id': category.id}

        url = detail_url(post.id)
        self.client.put(url, payload)
        post.refresh_from_db()
        self.assertEqual(post.title, payload['title'])
        self.assertEqual(post.content, payload['content'])
        self.assertEqual(post.category_id.id, payload['category_id'])
