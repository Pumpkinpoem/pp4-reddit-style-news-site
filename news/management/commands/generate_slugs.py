from django.core.management.base import BaseCommand
from news.models import Post
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Generate slugs for existing posts'

    def handle(self, *args, **kwargs):
        posts = Post.objects.filter(slug__isnull=True)
        for post in posts:
            post.slug = slugify(post.title)
            post.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully generated slug for post "{post.title}"'))
