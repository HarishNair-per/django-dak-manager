# Generated by Django 5.2 on 2025-05-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0004_furniture_thumbnail_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='thumbnail_new',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='thumbnails_new'),
        ),
    ]
