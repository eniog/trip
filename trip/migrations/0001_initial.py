# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('lat', models.DecimalField(max_digits=13, decimal_places=10)),
                ('lng', models.DecimalField(max_digits=13, decimal_places=10)),
            ],
        ),
    ]
