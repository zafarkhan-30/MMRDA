# Generated by Django 4.1.2 on 2022-11-22 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0005_alter_pap_date_of_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pap',
            name='date_of_notification',
        ),
    ]