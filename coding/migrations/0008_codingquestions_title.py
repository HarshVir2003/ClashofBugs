# Generated by Django 5.0 on 2024-02-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0007_remove_codingquestions_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='codingquestions',
            name='title',
            field=models.TextField(default='jass'),
            preserve_default=False,
        ),
    ]
