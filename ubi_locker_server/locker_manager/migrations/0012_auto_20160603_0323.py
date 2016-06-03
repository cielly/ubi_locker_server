# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0011_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='pic',
            field=models.ImageField(default=b'admin/none.jpg', upload_to=b'admin'),
        ),
    ]
