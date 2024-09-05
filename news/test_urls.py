from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import index, post_detail

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_post_detail_url_resolves(self):
        url = reverse('post_detail', args=['test-post'])
        self.assertEqual(resolve(url).func, post_detail)
