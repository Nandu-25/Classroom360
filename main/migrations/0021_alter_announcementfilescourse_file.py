# Generated by Django 4.2.5 on 2023-11-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_announcementfilescourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcementfilescourse',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='announce/'),
        ),
    ]
