# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaas_app', '0002_auto_20141013_2014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ad_details',
            new_name='ad_detail',
        ),
    ]
