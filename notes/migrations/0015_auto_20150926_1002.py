# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0014_games_sponsor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='due',
            new_name='join_date',
        ),
        migrations.RemoveField(
            model_name='note',
            name='done',
        ),
    ]
