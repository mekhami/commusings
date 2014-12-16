# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141211_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='teaser',
            field=models.CharField(default=b'', max_length=200, null=True),
            preserve_default=True,
        ),
    ]
