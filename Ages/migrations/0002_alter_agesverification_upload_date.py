# Generated by Django 3.2.25 on 2024-03-14 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agesverification',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 14, 12, 9, 4, 410368)),
        ),
    ]
