# Generated by Django 3.2.5 on 2022-08-08 16:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0002_auto_20220808_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='user',
        ),
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
