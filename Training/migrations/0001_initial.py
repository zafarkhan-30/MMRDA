# Generated by Django 4.1.2 on 2022-12-01 06:35

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='photographs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photograph_title', models.CharField(blank=True, max_length=255, null=True)),
                ('photographs_uploaded_by', models.CharField(blank=True, max_length=100, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('site_photographs', models.ImageField(blank=True, null=True, upload_to='site_photographs/')),
            ],
        ),
        migrations.CreateModel(
            name='traning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('traning_title', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('no_of_attends', models.IntegerField(blank=True, null=True)),
                ('male', models.CharField(blank=True, max_length=255, null=True)),
                ('female', models.CharField(blank=True, max_length=255, null=True)),
                ('incharge_person', models.CharField(blank=True, max_length=253, null=True)),
                ('traninig_initiated_by', models.CharField(blank=True, choices=[('GC (Genral Contractor)', 'GC (Genral Contractor)'), ('Consultant', 'Consultant'), ('MMRDA', 'MMRDA')], max_length=255, null=True)),
                ('conduct_date', models.DateField(auto_now=True, null=True)),
                ('traning_date', models.DateField(auto_now=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('photographs', models.ImageField(blank=True, null=True, upload_to='traning_photographs/')),
                ('traning_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
