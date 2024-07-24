import json
from django.core.management.base import BaseCommand
from news.models import Category

class Command(BaseCommand):
    help = 'Load categories from a JSON file'

    def handle(self, *args, **kwargs):
        with open('data/categories.json') as file:
            categories = json.load(file)
            for category_data in categories:
                category, created = Category.objects.get_or_create(name=category_data['name'])
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Category "{category.name}" created.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Category "{category.name}" already exists.'))
