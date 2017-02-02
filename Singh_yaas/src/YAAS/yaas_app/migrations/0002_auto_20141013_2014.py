# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('yaas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad_details',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date(2014, 10, 13), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad_details',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
