# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0017_auto_20150927_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='color',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='games',
            name='color',
        ),
        migrations.RemoveField(
            model_name='games',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='note',
            name='color',
        ),
        migrations.RemoveField(
            model_name='note',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='color',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='color',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='fontcolor',
        ),
    ]
