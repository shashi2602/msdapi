# Generated by Django 3.1 on 2020-08-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_bowlingaverages'),
    ]

    operations = [
        migrations.AddField(
            model_name='batfiledaverages',
            name='Best',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bowlingaverages',
            name='Best',
            field=models.CharField(default='', max_length=200),
        ),
    ]