# Generated by Django 4.1.2 on 2022-12-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnvMonitoring', '0005_rename_date_air_dateofconduct_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treemanagment',
            old_name='Cutting_details',
            new_name='botanicalName',
        ),
        migrations.RenameField(
            model_name='treemanagment',
            old_name='Management',
            new_name='commanName',
        ),
        migrations.RenameField(
            model_name='treemanagment',
            old_name='botanical_name',
            new_name='management',
        ),
        migrations.RenameField(
            model_name='treemanagment',
            old_name='No_of_trees_cut',
            new_name='noOfTreeCut',
        ),
        migrations.RenameField(
            model_name='treemanagment',
            old_name='survey_date',
            new_name='surveyDate',
        ),
        migrations.RenameField(
            model_name='treemanagment',
            old_name='survey_time',
            new_name='surveyTime',
        ),
        migrations.RenameField(
            model_name='treemanagment',
            old_name='common_name',
            new_name='transplantedDetails',
        ),
        migrations.RenameField(
            model_name='treemanagment',
            old_name='transplanted_details',
            new_name='treecutDetails',
        ),
        migrations.AddField(
            model_name='treemanagment',
            name='photographs',
            field=models.ImageField(blank=True, null=True, upload_to='treemanegment_photos/'),
        ),
        migrations.AlterField(
            model_name='wastetreatments',
            name='wastehandling',
            field=models.CharField(blank=True, choices=[('Disposal', 'Disposal'), ('Dumped', 'Dumped'), ('Transportation', 'Transportation'), ('Recycling', 'Recycling')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wastetreatments',
            name='wastetype',
            field=models.CharField(blank=True, choices=[('Hazardous Waste', 'Hazardous'), ('Bio Waste', 'Bio'), ('Electrical Waste', 'Electrical'), ('Non-Bio waste', 'Non-Bio')], max_length=255, null=True),
        ),
    ]
