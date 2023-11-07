from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_posts(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count  = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostDetailView(APITestCase):
    det setUp(self):
    adam = User.objects.create_user(username='adam', password='pass')
    brian = User.objects.create_user(username='brian', password='pass')
    Post.objects.create(
        owner=adam, title='a title', content='adams content'
    )
    Post.objects.create(
        owner=brian, title='a title', content='brians content'
    )

def test_can_retrieve_post_using_valid_id(self):
    response = self.client.get('/posts/1/')
    