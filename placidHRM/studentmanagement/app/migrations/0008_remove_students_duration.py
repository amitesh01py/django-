# Generated by Django 4.0.5 on 2022-08-01 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_students_fees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='duration',
        ),
    ]
