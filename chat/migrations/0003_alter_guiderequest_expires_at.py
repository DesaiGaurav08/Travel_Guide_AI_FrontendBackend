# Generated by Django 5.0 on 2024-12-29 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_guiderequest_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guiderequest',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 29, 14, 28, 0, 822692, tzinfo=datetime.timezone.utc)),
        ),
    ]
