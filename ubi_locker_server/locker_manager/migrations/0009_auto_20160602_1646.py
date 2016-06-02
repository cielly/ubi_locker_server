# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0008_auto_20160602_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekday',
            name='access',
        ),
        migrations.AddField(
            model_name='access',
            name='day',
            field=models.ManyToManyField(to='locker_manager.Weekday'),
        ),
    ]
