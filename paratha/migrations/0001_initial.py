# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-26 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('xcor', models.DecimalField(decimal_places=4, default=b'', max_digits=10)),
                ('ycor', models.DecimalField(decimal_places=4, default=b'', max_digits=10)),
                ('capacity', models.IntegerField(default=200)),
            ],
        ),
    ]
