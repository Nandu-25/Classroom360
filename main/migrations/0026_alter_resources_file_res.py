# Generated by Django 4.2.5 on 2023-11-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_resources_file_res'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='file_res',
            field=models.FileField(blank=True, null=True, upload_to='resources/'),
        ),
    ]
