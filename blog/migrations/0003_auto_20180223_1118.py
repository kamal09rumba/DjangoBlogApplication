# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180223_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.ForeignKey(related_name='subcategory', blank=True, to='blog.Category'),
        ),
    ]
