# Generated by Django 3.2.7 on 2021-09-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.URLField(blank=True, null=True),
        ),
    ]
