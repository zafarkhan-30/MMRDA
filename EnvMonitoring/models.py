from django.db import models
from Auth.models import User
from django.db.models.signals import post_save
from django.contrib.gis.db import models
# Create your models here.


# class EnvMonitoring(models.Model):
#     env_monitoring = models.ForeignKey(
#         User, related_name="Quality_Monitoring", on_delete=models.CASCADE , null=True   , blank=True)
#     choices = [('CA-07', 'CA-07'), ('CA-10', 'CA-10'), ('CA-09', 'CA-09')]
#     package = models.CharField(
#         max_length=255, choices=choices, null=True, blank=True)

#     def __str__(self) -> str:
#         return self.env_monitoring.email


# class EnvQualityMonitoring(models.Model):
#     eqm_id = models.OneToOneField(
#         EnvMonitoring, related_name='EnvQualityMonitoring', on_delete=models.CASCADE , null=True   , blank=True)

#     def __str__(self) -> str:
#         return self.eqm_id.env_monitoring.email
# def create_data(sender, instance, **kwargs):
#     if kwargs['created']:
#         created = EnvQualityMonitoring.objects.create(eqm_id=instance)
# post_save.connect(create_data, sender=EnvMonitoring)


# Abstarct Baseclass for EnvMonitoring for common field
class Baseclass(models.Model):
    choices = [('JAN-MAR 2022', 'JAN-MAR 2022'), ('APR-JUN 2022', 'APR-JUN 2022'),
               ('JULY-AUG 2022', 'JULY-AUG 2022')]
    quarter = models.CharField(
        max_length=255, choices=choices, null=True, blank=True)
    package_choice = [('CA-08', 'CA-08'), ('CA-09', 'CA-09'), ('CA-10', 'CA-10'),
                      ('CA-11', 'CA-11'), ('CA-12', 'CA-12'), ('CA-54', 'CA-54')]
    package = models.CharField(
        max_length=255, choices=package_choice,  null=True, blank=True)
    # latitude = models.IntegerField(null=True, blank=True)
    # longitude = models.IntegerField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    date = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Air(Baseclass):
    # air_id = models.ForeignKey(
    #     EnvQualityMonitoring, related_name='airs', on_delete=models.CASCADE , null= True   , blank=True)
    standard = models.FloatField(max_length=255, null=True, blank=True)
    deviation = models.FloatField(max_length=255, null=True, blank=True)
    trends = models.CharField(max_length=100, blank=True, null=True)




class water(Baseclass):
    # water_id = models.ForeignKey(
        # EnvQualityMonitoring, related_name='waters', on_delete=models.CASCADE , null= True   , blank=True)
    # Water = [('GroundWater', 'Ground Water'), ('SeaWater', 'Sea Water'), ]
    quality_of_water = models.CharField(max_length=255, null=True, blank=True)
    source_of_water = models.CharField(max_length=255, null=True, blank=True)

    


class Noise(Baseclass):
    # noise_id = models.ForeignKey(
    #     EnvQualityMonitoring, related_name="noises", on_delete=models.CASCADE , null =True   , blank=True )
    noise_level = models.CharField(max_length=255, null=True, blank=True)
    period = [("1 hour", "1 hour"), ("3 hours", "3 hours"),
              ("6 hours", "6 hours"), ]
    Monitoring_Period = models.CharField(
        max_length=255, choices=period, null=True, blank=True)

    # def __str__(self) -> str:
    #     return "filled By :- " + self.noise_id.eqm_id.env_monitoring.email


class TreeManagment(Baseclass):
    # tree_id = models.ForeignKey(
        # EnvMonitoring, related_name='EnvironmentalMonitoring', on_delete=models.CASCADE, null=True, blank=True )
    tree_no= models.BigAutoField(primary_key= True , auto_created=True)
    common_name = models.CharField(max_length=255 , blank=True, null=True)
    botanical_name = models.CharField(max_length=255 , null= True, blank=True) 
    condition = models.CharField(max_length=255, null =True, blank=True)
    survey_date = models.DateField(null = True, blank = True )
    survey_time = models.TimeField(null = True, blank = True)
    planted = models.BooleanField()
    planted_details = models.CharField(max_length=255, null=True, blank=True)
    No_of_trees_cut = models.IntegerField(null=True, blank=True)
    Cutting_details = models.CharField(max_length=255, null=True, blank=True)
    transplanted = models.BooleanField()
    transplanted_details = models.CharField(
        max_length=255, null=True, blank=True)
    Management = models.CharField(max_length=255,  null=True, blank=True)

    # def str(self):
    #     return self.tree_id.env_monitoring.email

class WasteTreatments(Baseclass):
    # waste_id = models.ForeignKey(
    #     EnvMonitoring, related_name="waste_treatments", on_delete=models.CASCADE, null=True, blank=True)
    _type = [('Hazardous Waste', 'Hazardous'), ('Bio Waste', 'Bio'),
             ('electronic waste', 'Electronic'), ]
    waste_type = models.CharField(max_length=255, choices=_type)
    choices = [('disposal', 'disposal'), ('Dumped', 'Dumped'), ('Transported to another location', 'Transported to another location'),
               ('recycle', 'recycle')]
    quantity = models.IntegerField(null=True, blank=True)
    waste_handled = models.CharField(
        max_length=255, choices=choices, blank=True, null=True)
    waste_handled_details = models.CharField(
        max_length=255, blank=True, null=True)
    photographs = models.ImageField(null=True, blank=True)
    documents = models.FileField(null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)



class MaterialSourcing(Baseclass):
    # materialsourcing_id = models.ForeignKey(
    #     EnvMonitoring, related_name="MaterialSourcing", on_delete=models.CASCADE, null=True, blank=True)
    source = [('Mines', 'Mines'), ('Blast', 'Blast')]
    approvals = models.FileField(null=True , blank= True )
    source_of_quary = models.CharField(max_length=255, choices=source)

    # def __str__(self) -> str:
    #     return self.materialsourcing_id.env_monitoring.email