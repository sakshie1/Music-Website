# Generated by Django 5.0 on 2024-01-28 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_song_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='cat',
        ),
    ]