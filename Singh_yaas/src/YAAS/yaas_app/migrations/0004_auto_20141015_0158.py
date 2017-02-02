# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaas_app', '0003_auto_20141014_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_detail',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published'),
        ),
    ]
