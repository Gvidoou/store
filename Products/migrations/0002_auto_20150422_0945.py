# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='crated_at',
            new_name='created_at',
        ),
    ]
