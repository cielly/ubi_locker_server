# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0007_auto_20160522_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday', models.CharField(max_length=50, choices=[(1, b'segunda-feira'), (2, b'terca-feira'), (3, b'quarta-feira'), (4, b'quinta-feira'), (5, b'sexta-feira'), (6, b'sabado'), (7, b'domingo')])),
                ('access', models.ForeignKey(to='locker_manager.Access')),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='pic',
            field=models.ImageField(default=b'static/imgs/admin/none.jpg', upload_to=b'static/imgs/admin'),
        ),
    ]
