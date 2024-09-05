from django.test import TestCase
from django.contrib.auth.models import User
from news.models import Post, Category

class PostModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name="Test Category")
        self.post = Post.objects.create(
            title="Test Post",
            author=self.user,
            content="This is a test post.",
            category=self.category
        )

    def test_slug_creation(self):
        self.assertEqual(self.post.slug, "test-post")

    def test_upvotes(self):
        self.post.upvotes.add(self.user)
        self.assertEqual(self.post.total_upvotes(), 1)

    def test_downvotes(self):
        self.post.downvotes.add(self.user)
        self.assertEqual(self.post.total_downvotes(), 1)
