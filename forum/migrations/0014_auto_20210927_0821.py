# Generated by Django 3.2.7 on 2021-09-27 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_auto_20210927_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commenter',
            new_name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
