# Generated by Django 4.2.2 on 2023-07-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0032_empexperience_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='empexperience',
            name='salary',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]