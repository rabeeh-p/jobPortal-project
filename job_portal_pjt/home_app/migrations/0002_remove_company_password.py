# Generated by Django 4.2.2 on 2023-06-17 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='password',
        ),
    ]