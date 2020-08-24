# Generated by Django 3.1 on 2020-08-22 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_hascaptain_ipl_worldcup'),
    ]

    operations = [
        migrations.CreateModel(
            name='worldcupscore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worldcupscore', to='base.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='wcscores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('M', models.CharField(max_length=200)),
                ('I', models.CharField(max_length=200)),
                ('NO', models.CharField(max_length=200)),
                ('R', models.CharField(max_length=200)),
                ('HS', models.CharField(max_length=200)),
                ('_100s', models.CharField(max_length=200)),
                ('_50s', models.CharField(max_length=200)),
                ('_4s6s', models.CharField(max_length=200)),
                ('Avg', models.CharField(max_length=200)),
                ('SR', models.CharField(max_length=200)),
                ('Ct', models.CharField(max_length=200)),
                ('St', models.CharField(max_length=200)),
                ('wc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worldcupscore', to='base.worldcupscore')),
            ],
        ),
    ]