# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker_manager', '0005_auto_20160510_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('status', models.CharField(max_length=200)),
                ('locker', models.ForeignKey(to='locker_manager.Locker')),
                ('person', models.ForeignKey(to='locker_manager.Person')),
            ],
        ),
        migrations.AddField(
            model_name='Admin',
            name='pic',
            field=models.ImageField(default=b'static/imgs/Admin/none.jpg', upload_to=b'static/imgs/Admin'),
        ),
        migrations.AlterField(
            model_name='access',
            name='final_time',
            field=models.TimeField(help_text=b'Please use the following format: <em>HH:MM</em>.'),
        ),
        migrations.AlterField(
            model_name='access',
            name='initial_time',
            field=models.TimeField(help_text=b'Please use the following format: <em>HH:MM</em>.'),
        ),
    ]
