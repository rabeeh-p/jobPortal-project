# Generated by Django 4.2.2 on 2023-07-12 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0025_marital'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='marital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home_app.marital'),
            preserve_default=False,
        ),
    ]
