# Generated by Django 4.1.2 on 2022-11-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0007_pap_date_of_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructionsitedetails',
            name='Medical_facility',
        ),
        migrations.RemoveField(
            model_name='labourcampdetails',
            name='Medical_facility',
        ),
        migrations.AddField(
            model_name='constructionsitedetails',
            name='Availability_Of_Doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constructionsitedetails',
            name='Availability_Of_First_aid_Kit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constructionsitedetails',
            name='Regular_Health_Checkup',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='labourcampdetails',
            name='Availability_Of_Doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='labourcampdetails',
            name='Availability_Of_First_aid_Kit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='labourcampdetails',
            name='Regular_Health_Checkup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pap',
            name='date_of_notification',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]