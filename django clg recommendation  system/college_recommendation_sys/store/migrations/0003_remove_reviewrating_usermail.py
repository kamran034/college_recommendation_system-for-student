# Generated by Django 4.2.2 on 2023-10-25 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_reviewrating_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='usermail',
        ),
    ]
