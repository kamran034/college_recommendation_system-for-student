# Generated by Django 4.2.2 on 2023-09-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degree', '0002_alter_postd_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postd',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
    ]
