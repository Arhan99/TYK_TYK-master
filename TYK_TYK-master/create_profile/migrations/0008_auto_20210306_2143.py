# Generated by Django 2.2.19 on 2021-03-06 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0007_auto_20210306_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createneighbour',
            name='presence_animals',
            field=models.BooleanField(default=False, verbose_name='Наличие животных'),
        ),
        migrations.AlterField(
            model_name='createneighbour',
            name='presence_flat',
            field=models.BooleanField(default=False, verbose_name='Наличие квартиры'),
        ),
    ]
