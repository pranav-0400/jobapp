# Generated by Django 4.2.5 on 2023-09-10 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 9, 10, 4, 57, 16, 322974, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
