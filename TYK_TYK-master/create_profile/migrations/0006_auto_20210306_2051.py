# Generated by Django 2.2.19 on 2021-03-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0005_auto_20210306_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbusiness',
            name='text_info_bus',
            field=models.TextField(blank=True, max_length=255, verbose_name='Информация'),
        ),
    ]
