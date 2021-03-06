# Generated by Django 2.0.7 on 2018-07-17 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotplot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DotPlotStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField()),
                ('year', models.PositiveIntegerField()),
                ('rate', models.FloatField()),
                ('count', models.PositiveIntegerField()),
                ('median', models.FloatField()),
            ],
            options={
                'managed': False,
            },
        ),
    ]
