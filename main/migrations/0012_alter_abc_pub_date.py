# Generated by Django 4.0.4 on 2022-05-18 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_abc_pub_date_alter_abc_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abc',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 12, 59, 54, 69665, tzinfo=utc), verbose_name='Дата'),
        ),
    ]
