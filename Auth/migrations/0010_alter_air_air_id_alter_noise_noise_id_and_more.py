# Generated by Django 4.1.2 on 2022-11-16 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0009_envmonitoring_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air',
            name='air_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airs', to='Auth.envqualitymonitoring'),
        ),
        migrations.AlterField(
            model_name='noise',
            name='noise_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noises', to='Auth.envqualitymonitoring'),
        ),
        migrations.AlterField(
            model_name='water',
            name='water_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waters', to='Auth.envqualitymonitoring'),
        ),
        migrations.CreateModel(
            name='TreeManagment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.CharField(max_length=255)),
                ('package', models.CharField(max_length=255)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('planted', models.BooleanField()),
                ('planted_details', models.CharField(max_length=255)),
                ('No_of_trees_cut', models.IntegerField()),
                ('Cutting_details', models.CharField(max_length=255)),
                ('transplanted', models.BooleanField()),
                ('transplanted_details', models.CharField(max_length=255)),
                ('Management', models.CharField(max_length=255)),
                ('tree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EnvironmentalMonitoring', to='Auth.envmonitoring')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
