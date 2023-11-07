# Generated by Django 4.2.5 on 2023-11-04 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_grades_is_graded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='end_datetime',
        ),
        migrations.AddField(
            model_name='course',
            name='max_classes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='students',
            field=models.ManyToManyField(related_name='roomsStu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='roomsTea', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_pre', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendCards', to='main.course')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendCards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]