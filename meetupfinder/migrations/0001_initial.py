# Generated by Django 3.1 on 2020-10-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_text', models.CharField(max_length=200)),
                ('event_date', models.DateTimeField(default='1234-12-12')),
            ],
        ),
    ]
