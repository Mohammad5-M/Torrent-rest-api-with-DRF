# Generated by Django 4.0.5 on 2022-06-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torran_api', '0007_remove_files_torrent_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='size',
            field=models.CharField(max_length=10),
        ),
    ]
