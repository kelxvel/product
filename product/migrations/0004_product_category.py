# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20150928_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=datetime.datetime(2015, 9, 28, 18, 50, 5, 801709, tzinfo=utc), to='product.Category'),
            preserve_default=False,
        ),
    ]
