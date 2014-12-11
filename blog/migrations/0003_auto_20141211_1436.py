# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141209_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 19, 36, 6, 779213, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=56),
            preserve_default=True,
        ),
    ]
