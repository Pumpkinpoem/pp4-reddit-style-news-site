from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from news.models import Post, Category

class PostViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name="Test Category")
        self.post = Post.objects.create(
            title="Test Post",
            author=self.user,
            content="This is a test post.",
            category=self.category
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_post'), {
        'title': 'New Post',
        'content': 'This is a new post.',
        'category': self.category.id
        }, follow=True)
        self.assertEqual(response.status_code, 200)  # Follow the redirect and expect 200 or 302

