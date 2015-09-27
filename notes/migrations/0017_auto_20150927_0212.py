# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0016_auto_20150926_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='Games',
            field=models.ManyToManyField(related_name='notes', null=True, to='notes.Games', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='Sponsor',
            field=models.ForeignKey(related_name='notes', blank=True, to='notes.Sponsor', null=True),
            preserve_default=True,
        ),
    ]
