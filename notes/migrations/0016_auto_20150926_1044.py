# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0015_auto_20150926_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='note',
            name='tag',
        ),
    ]
