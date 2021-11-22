from django.contrib.auth.models import User
from django.test import TestCase, Client
from bs4 import BeautifulSoup
from blog.models import Post


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_trump = User.objects.create(username='trump', password='somepassword')

    def test_landing(self):
        post_001 = Post.objects.create(
            title='1st post',
            content='it is 1st post.',
            author=self.user_trump
        )

        post_002 = Post.objects.create(
            title='2nd post',
            content='it is 2nd post.',
            author=self.user_trump
        )

        post_003 = Post.objects.create(
            title='3rd post',
            content='it is 3rd post.',
            author=self.user_trump
        )

        post_004 = Post.objects.create(
            title='4th post',
            content='it is 4th post.',
            author=self.user_trump
        )

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        body = soup.body
        self.assertNotIn(post_001.title, body.text)
        self.assertIn(post_002.title, body.text)
        self.assertIn(post_003.title, body.text)
        self.assertIn(post_004.title, body.text)
