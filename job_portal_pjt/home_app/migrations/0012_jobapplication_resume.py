# Generated by Django 4.2.2 on 2023-06-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0011_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='resume',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
