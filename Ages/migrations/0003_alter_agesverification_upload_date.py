# Generated by Django 3.2.25 on 2024-04-05 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ages', '0002_alter_agesverification_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agesverification',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 5, 9, 3, 12, 932726)),
        ),
    ]
