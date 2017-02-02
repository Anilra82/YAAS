# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaas_app', '0004_auto_20141015_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_detail',
            name='details',
            field=models.CharField(max_length=1000),
        ),
    ]
