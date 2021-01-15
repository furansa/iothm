# Generated by Django 3.1.5 on 2021-01-15 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'sensor_types',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.sensortypes')),
            ],
            options={
                'db_table': 'sensors',
                'ordering': ['id'],
            },
        ),
    ]
