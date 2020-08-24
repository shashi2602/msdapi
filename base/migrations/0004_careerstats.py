# Generated by Django 3.1 on 2020-08-21 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_domesticinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careerstats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_name', models.CharField(max_length=200)),
                ('Matches', models.CharField(max_length=200)),
                ('Runs_scored', models.CharField(max_length=200)),
                ('Batting_average', models.CharField(max_length=200)),
                ('top_100s_50s', models.CharField(max_length=200)),
                ('Top_score', models.CharField(max_length=200)),
                ('Balls_bowled', models.CharField(max_length=200)),
                ('Wickets', models.CharField(max_length=200)),
                ('Bowling_average', models.CharField(max_length=200)),
                ('top_5_wickets_in_innings', models.CharField(max_length=200)),
                ('top_10_wickets_in_match', models.CharField(max_length=200)),
                ('Best_bowling', models.CharField(max_length=200)),
                ('Catches_and_stumpings', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='careerstats', to='base.personalinfo')),
            ],
        ),
    ]
