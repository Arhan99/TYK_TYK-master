# Generated by Django 2.2.19 on 2021-03-08 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0029_auto_20210308_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createneighbour',
            name='user_neig',
            field=models.ForeignKey(auto_created=True, blank=True, default='auth.User', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
