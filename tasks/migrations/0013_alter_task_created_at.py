# Generated by Django 3.2.3 on 2021-06-20 08:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20210620_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 8, 43, 16, 217204, tzinfo=utc)),
        ),
    ]
