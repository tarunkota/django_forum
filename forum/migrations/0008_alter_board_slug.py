# Generated by Django 3.2.7 on 2021-09-27 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20210926_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
