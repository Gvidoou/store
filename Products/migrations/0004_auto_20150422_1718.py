# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='title',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
