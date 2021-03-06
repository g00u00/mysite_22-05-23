# Generated by Django 4.0.4 on 2022-05-14 15:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_abc_a_alter_abc_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
        migrations.AlterField(
            model_name='abc',
            name='a',
            field=models.IntegerField(default=0, verbose_name='A'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='b',
            field=models.IntegerField(default=0, verbose_name='B'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='c',
            field=models.IntegerField(default=0, verbose_name='C'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 14, 15, 47, 39, 115938, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='task',
            field=models.CharField(default='Равна ли С сумме A и B?', max_length=256, verbose_name='Задание'),
        ),
    ]
