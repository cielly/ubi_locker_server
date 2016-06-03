# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0010_auto_20160602_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='locker_manager.Person')),
                ('program', models.CharField(default=b'', max_length=100)),
                ('name', models.CharField(default=b'', max_length=200)),
            ],
            bases=('locker_manager.person',),
        ),
    ]
