# Generated by Django 4.1.2 on 2022-11-24 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EnvMonitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treemanagment',
            name='tree_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EnvironmentalMonitoring', to='EnvMonitoring.envmonitoring'),
        ),
    ]
