# Generated by Django 5.0 on 2024-01-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_audiofile_cat_audiofile_is_active_audiofile_pimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('singer', models.CharField(max_length=500)),
                ('pimage', models.ImageField(upload_to='image')),
                ('audio_file', models.FileField(upload_to='audio_files')),
            ],
        ),
    ]
