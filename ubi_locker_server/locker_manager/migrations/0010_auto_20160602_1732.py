# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0009_auto_20160602_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='weekday',
            field=models.CharField(max_length=50, choices=[(b'1', b'segunda-feira'), (b'2', b'terca-feira'), (b'3', b'quarta-feira'), (b'4', b'quinta-feira'), (b'5', b'sexta-feira'), (b'6', b'sabado'), (b'7', b'domingo')]),
        ),
    ]
