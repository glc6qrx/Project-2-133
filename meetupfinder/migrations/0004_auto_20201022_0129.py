# Generated by Django 3.2.dev20200902131603 on 2020-10-22 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetupfinder', '0003_auto_20201021_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_event_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='end event date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='event date'),
        ),
    ]
