# Generated by Django 5.0 on 2024-02-01 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0003_buttonclick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermatching',
            name='status',
        ),
    ]
