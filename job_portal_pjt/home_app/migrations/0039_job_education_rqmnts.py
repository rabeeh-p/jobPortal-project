# Generated by Django 4.2.2 on 2023-07-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0038_remove_job_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='education_rqmnts',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]