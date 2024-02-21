# Generated by Django 5.0 on 2024-01-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='Avatar',
            field=models.CharField(default='hi', max_length=24),
            preserve_default=False,
        ),
    ]
