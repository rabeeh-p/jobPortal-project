# Generated by Django 4.2.2 on 2023-07-19 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0052_applyjob_is_conform'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='custom_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
