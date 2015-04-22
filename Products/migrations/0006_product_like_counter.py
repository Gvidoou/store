# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_comments_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like_counter',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
