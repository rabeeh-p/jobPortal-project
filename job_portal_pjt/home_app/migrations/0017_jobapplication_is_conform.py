# Generated by Django 4.2.2 on 2023-06-30 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0016_company_is_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='is_conform',
            field=models.BooleanField(default=False),
        ),
    ]