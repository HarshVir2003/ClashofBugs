# Generated by Django 5.0 on 2024-02-10 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0006_alter_codingquestions_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codingquestions',
            name='title',
        ),
    ]