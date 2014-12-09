# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2014, 12, 9, 0, 17, 11, 265546, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='teaser',
            field=models.TextField(default=datetime.datetime(2014, 12, 9, 0, 17, 13, 889696, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
