# Generated by Django 4.2.2 on 2023-06-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_remove_company_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_finished',
            field=models.BooleanField(default=True),
        ),
    ]
