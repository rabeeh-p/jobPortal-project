# Generated by Django 4.2.2 on 2023-07-18 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0043_remove_company_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
    ]
