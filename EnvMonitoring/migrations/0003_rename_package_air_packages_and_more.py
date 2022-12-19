# Generated by Django 4.1.2 on 2022-12-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnvMonitoring', '0002_rename_waste_handled_details_wastetreatments_wastehandlinglocation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='air',
            old_name='package',
            new_name='packages',
        ),
        migrations.RenameField(
            model_name='materialsourcing',
            old_name='package',
            new_name='packages',
        ),
        migrations.RenameField(
            model_name='materialsourcing',
            old_name='source_of_quary',
            new_name='sourceOfQuarry',
        ),
        migrations.RenameField(
            model_name='noise',
            old_name='package',
            new_name='packages',
        ),
        migrations.RenameField(
            model_name='treemanagment',
            old_name='package',
            new_name='packages',
        ),
        migrations.RenameField(
            model_name='wastetreatments',
            old_name='package',
            new_name='packages',
        ),
        migrations.RenameField(
            model_name='water',
            old_name='package',
            new_name='packages',
        ),
        migrations.AddField(
            model_name='materialsourcing',
            name='typeOfMaterial',
            field=models.CharField(blank=True, choices=[('Material A', 'Material A'), ('Material B', 'Material B'), ('Material C', 'Material C'), ('Material D', 'Material D')], max_length=255, null=True),
        ),
    ]
