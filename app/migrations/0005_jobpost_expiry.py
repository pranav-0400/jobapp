# Generated by Django 4.2.5 on 2023-09-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_jobpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='expiry',
            field=models.DateField(null=True),
        ),
    ]
