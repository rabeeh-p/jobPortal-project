# Generated by Django 4.2.2 on 2023-07-12 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0023_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home_app.gender'),
            preserve_default=False,
        ),
    ]