# Generated by Django 4.2.2 on 2023-07-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0046_company_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
