# Generated by Django 4.2.2 on 2023-07-26 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0053_applyjob_custom_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='skills',
        ),
    ]
