# Generated by Django 3.2.6 on 2021-09-04 17:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lend', '0002_alter_transaction_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 4, 17, 28, 29, 215421, tzinfo=utc), verbose_name='created at'),
        ),
    ]
