# Generated by Django 4.2.2 on 2023-09-09 15:39

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collegepost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('text', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
            ],
        ),
    ]