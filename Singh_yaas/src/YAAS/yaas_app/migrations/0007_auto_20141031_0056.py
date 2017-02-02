# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('yaas_app', '0006_auction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='deadline',
            new_name='enddate',
        ),
        migrations.RenameField(
            model_name='auction',
            old_name='min_price',
            new_name='price',
        ),
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.CharField(default=datetime.date(2014, 10, 31), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auction',
            name='startdate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
