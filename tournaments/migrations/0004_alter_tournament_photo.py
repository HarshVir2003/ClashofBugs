# Generated by Django 5.0 on 2024-02-20 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_alter_tournament_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='Photo',
            field=models.URLField(),
        ),
    ]