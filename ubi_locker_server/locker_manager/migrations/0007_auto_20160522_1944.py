# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0006_auto_20160521_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='locker_password',
            field=models.CharField(help_text=b'4-Digit password used to unlock the locker', max_length=50),
        ),
    ]
