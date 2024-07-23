# Generated by Django 5.0.6 on 2024-07-23 07:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='downvoted_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='upvoted_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]