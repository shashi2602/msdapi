# Generated by Django 3.1 on 2020-08-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='desc',
            field=models.TextField(),
        ),
    ]
