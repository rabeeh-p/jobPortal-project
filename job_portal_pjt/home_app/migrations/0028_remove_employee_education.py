# Generated by Django 4.2.2 on 2023-07-12 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0027_rename_marital_employee_marital_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='education',
        ),
    ]
