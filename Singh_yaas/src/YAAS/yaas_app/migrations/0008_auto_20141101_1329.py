# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaas_app', '0007_auto_20141031_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
