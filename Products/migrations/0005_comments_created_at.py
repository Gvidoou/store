# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_auto_20150422_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 18, 2, 18, 217149, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
