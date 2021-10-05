# Generated by Django 3.2.7 on 2021-09-26 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swforumable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0003_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('text', models.TextField(blank=True, max_length=5000, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='post_photos/', verbose_name='Add image (optional)')),
                ('video', models.FileField(blank=True, null=True, upload_to='post_videos/', verbose_name='Add video (optional)')),
                ('points', models.FloatField(default=0.0)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('upvotes', models.IntegerField(default=1)),
                ('downvotes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='forum.board')),
                ('liked_by', models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
