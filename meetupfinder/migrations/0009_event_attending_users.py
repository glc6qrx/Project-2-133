# Generated by Django 3.1 on 2020-11-06 12:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetupfinder', '0008_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attending_users',
            field=models.ManyToManyField(blank=True, related_name='attending_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
