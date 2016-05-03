# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locker_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('initial_time', models.TimeField()),
                ('final_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locker_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matriculation', models.PositiveIntegerField()),
                ('locker_password', models.CharField(max_length=50)),
                ('RFID', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='locker_manager.Person')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('locker_manager.person',),
        ),
        migrations.AddField(
            model_name='access',
            name='locker',
            field=models.ForeignKey(to='locker_manager.Locker'),
        ),
        migrations.AddField(
            model_name='access',
            name='person',
            field=models.ForeignKey(to='locker_manager.Person'),
        ),
    ]
