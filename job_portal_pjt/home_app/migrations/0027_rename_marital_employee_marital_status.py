# Generated by Django 4.2.2 on 2023-07-12 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0026_employee_marital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='marital',
            new_name='marital_status',
        ),
    ]