# Generated by Django 2.2.19 on 2021-03-13 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0053_createbusiness_user_bus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createbusiness',
            options={'ordering': ['-id'], 'verbose_name': 'Бизенс', 'verbose_name_plural': 'Бизнесы'},
        ),
    ]
