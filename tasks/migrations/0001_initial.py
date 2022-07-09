# Generated by Django 3.2.6 on 2021-09-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=225)),
                ('contact_details', models.CharField(max_length=15)),
                ('Total_amount', models.PositiveBigIntegerField()),
                ('advance_amount', models.PositiveBigIntegerField()),
                ('pending_amount', models.PositiveBigIntegerField()),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]
