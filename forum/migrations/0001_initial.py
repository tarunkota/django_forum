# Generated by Django 3.2.7 on 2021-09-26 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('info', models.TextField()),
                ('url', models.URLField()),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=128, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=128)),
                ('lastname', models.CharField(blank=True, max_length=128)),
                ('dp', models.URLField(default='https://storage.googleapis.com/learnitbucket/Forum/defaults/dp.png')),
                ('bio', models.TextField(blank=True)),
                ('member_since', models.DateTimeField(default=django.utils.timezone.now)),
                ('badges', models.ManyToManyField(blank=True, to='forum.Badge')),
                ('contact_list', models.ManyToManyField(blank=True, related_name='contacters', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(blank=True, default=0, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('pending_list', models.ManyToManyField(blank=True, related_name='my_pending_requests', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
