# Generated by Django 5.2 on 2025-04-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip_ref', '0005_alter_reference_reply_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='reply_file',
            field=models.FileField(blank=True, default='reply/blank.pdf', null=True, upload_to='reply'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='subject_file',
            field=models.FileField(blank=True, default='subject/blank.pdf', null=True, upload_to='subject'),
        ),
    ]
