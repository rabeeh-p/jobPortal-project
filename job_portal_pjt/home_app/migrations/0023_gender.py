# Generated by Django 4.2.2 on 2023-07-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0022_employee_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=30)),
            ],
        ),
    ]
