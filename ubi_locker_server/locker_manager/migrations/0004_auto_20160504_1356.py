# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0003_auto_20160503_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='locker',
            name='room',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='Admin',
            name='user',
            field=models.OneToOneField(default=None, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
