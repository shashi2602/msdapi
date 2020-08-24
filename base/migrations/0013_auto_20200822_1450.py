# Generated by Django 3.1 on 2020-08-22 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_awards_awardname'),
    ]

    operations = [
        migrations.CreateModel(
            name='honours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('honour', models.CharField(max_length=1000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='honours', to='base.awards')),
            ],
        ),
        migrations.DeleteModel(
            name='Nationalhonours',
        ),
    ]
