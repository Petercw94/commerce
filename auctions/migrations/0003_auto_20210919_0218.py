# Generated by Django 3.2.5 on 2021-09-19 02:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 19, 2, 18, 26, 368286, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
