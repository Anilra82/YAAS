# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaas_app', '0008_auto_20141101_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='status',
            field=models.CharField(default=b'active', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='auction',
            name='description',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='enddate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='auction',
            name='startdate',
            field=models.DateTimeField(),
        ),
    ]
