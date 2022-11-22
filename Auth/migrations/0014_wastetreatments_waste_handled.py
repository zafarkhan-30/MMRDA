# Generated by Django 4.1.2 on 2022-11-18 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0013_occupationalhealthsafety'),
    ]

    operations = [
        migrations.AddField(
            model_name='wastetreatments',
            name='waste_handled',
            field=models.CharField(choices=[('disposal', 'disposal'), ('Dumped', 'Dumped'), ('Transported to another location', 'Transported to another location'), ('recycle', 'recycle')], default=None, max_length=255),
            preserve_default=False,
        ),
    ]
