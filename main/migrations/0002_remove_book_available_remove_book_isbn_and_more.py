# Generated by Django 5.1.3 on 2024-11-20 09:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='available',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='stock',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
