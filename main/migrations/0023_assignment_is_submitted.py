# Generated by Django 4.2.5 on 2023-11-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_assignment_assignmentsub'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
