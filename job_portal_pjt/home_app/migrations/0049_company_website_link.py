# Generated by Django 4.2.2 on 2023-07-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0048_remove_company_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='website_link',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]