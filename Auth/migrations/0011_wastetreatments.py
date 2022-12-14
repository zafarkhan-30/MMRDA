# Generated by Django 4.1.2 on 2022-11-16 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0010_alter_air_air_id_alter_noise_noise_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteTreatments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.CharField(max_length=255)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('waste_type', models.CharField(choices=[('Hazardous Waste', 'Hazardous'), ('Bio Waste', 'Bio'), ('electronic waste', 'Electronic')], max_length=255)),
                ('quantity', models.IntegerField()),
                ('package', models.CharField(max_length=255)),
                ('photographs', models.ImageField(null=True, upload_to='')),
                ('documents', models.FileField(null=True, upload_to='')),
                ('remarks', models.CharField(max_length=255)),
                ('waste_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waste_treatments', to='Auth.envmonitoring')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
