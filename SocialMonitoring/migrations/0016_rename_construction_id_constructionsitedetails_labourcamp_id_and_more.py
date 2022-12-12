# Generated by Django 4.1.2 on 2022-12-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0015_remove_labourcamp_transport_facility'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constructionsitedetails',
            old_name='construction_id',
            new_name='labourCamp_id',
        ),
        migrations.RemoveField(
            model_name='constructionsitedetails',
            name='date',
        ),
        migrations.RemoveField(
            model_name='constructionsitedetails',
            name='package',
        ),
        migrations.RemoveField(
            model_name='constructionsitedetails',
            name='quarter',
        ),
        migrations.RemoveField(
            model_name='labourcamp',
            name='camp_id',
        ),
        migrations.RemoveField(
            model_name='labourcampdetails',
            name='date',
        ),
        migrations.RemoveField(
            model_name='labourcampdetails',
            name='package',
        ),
        migrations.RemoveField(
            model_name='labourcampdetails',
            name='quarter',
        ),
        migrations.AddField(
            model_name='labourcamp',
            name='transport_facility',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]