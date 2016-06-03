# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0012_auto_20160603_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='pic',
            field=models.ImageField(default=b'upload/none.jpg', upload_to=b'upload'),
        ),
    ]
