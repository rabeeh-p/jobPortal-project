# Generated by Django 4.2.2 on 2023-07-17 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0039_job_education_rqmnts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='skills',
        ),
    ]
