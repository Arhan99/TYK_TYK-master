# Generated by Django 2.2.19 on 2021-03-14 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0060_auto_20210314_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbusiness',
            name='user_bus',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]