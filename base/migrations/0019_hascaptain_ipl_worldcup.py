# Generated by Django 3.1 on 2020-08-22 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20200822_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='worldcup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worldcup', to='base.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='IPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ipl', to='base.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Hascaptain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hascaptain', to='base.personalinfo')),
            ],
        ),
    ]
