# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_note_achievements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'red', max_length=50)),
                ('fontcolor', models.CharField(default=b'black', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'red', max_length=50)),
                ('fontcolor', models.CharField(default=b'black', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
