# Generated by Django 3.2.8 on 2021-10-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0023_rename_user_comment_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postType',
            field=models.CharField(choices=[('q', 'q'), ('t', 't'), ('v', 'v'), ('i', 'i'), ('l', 'l'), ('f', 'f')], default='t', max_length=1),
        ),
    ]
