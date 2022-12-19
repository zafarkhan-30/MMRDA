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
    choices = [('Jan-Mar 2022', 'Jan-Mar 2022'), ('Apr-Jun 2022',
                                                  'Apr-Jun 2022'), ('July-Aug 2022', 'July-Aug 2022')]
    quarter = models.CharField(
        max_length=255, choices=choices, null=True, blank=True)
    package_choice = [('CA-08', 'CA-08'), ('CA-09', 'CA-09'), ('CA-10', 'CA-10'),
                      ('CA-11', 'CA-11'), ('CA-12', 'CA-12'), ('CA-54', 'CA-54')]
    packages  = models.CharField(
        max_length=255, choices=package_choice,  null=True, blank=True)
    # latitude = models.IntegerField(null=True, blank=True)
    # longitude = models.IntegerField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    dateOfConduct   = models.DateField(null=True, blank=True)

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
    commanName  = models.CharField(max_length=255 , blank=True, null=True)
    botanicalName  = models.CharField(max_length=255 , null= True, blank=True) 
    condition  = models.CharField(max_length=255, null =True, blank=True)
    surveyDate  = models.DateField(null = True, blank = True )
    surveyTime  = models.TimeField(null = True, blank = True)
    planted = models.BooleanField(blank= True, null= True)
    plantedDetails  = models.CharField(max_length=255, null=True, blank=True)
    noOfTreeCut   = models.IntegerField(null=True, blank=True)
    treecutDetails   = models.CharField(max_length=255, null=True, blank=True)
    transplanted    = models.BooleanField(blank= True, null = True)
    transplantedDetails    = models.CharField(
        max_length=255, null=True, blank=True)
    management  = models.CharField(max_length=255,  null=True, blank=True)
    photographs = models.ImageField(upload_to="treemanegment_photos/" , null = True, blank = True)
    # def str(self):
    #     return self.tree_id.env_monitoring.email

class WasteTreatments(Baseclass):
    # waste_id = models.ForeignKey(
    #     EnvMonitoring, related_name="waste_treatments", on_delete=models.CASCADE, null=True, blank=True)
    _type = [('Hazardous Waste', 'Hazardous'), ('Bio Waste', 'Bio'), ('Electrical Waste' , 'Electrical') ,  ('Non-Bio waste', 'Non-Bio')]
    wastetype  = models.CharField(max_length=255, choices=_type , null= True, blank=True )
    choices = [('Disposal', 'Disposal'), ('Dumped', 'Dumped'), ('Transportation', 'Transportation'),
               ('Recycling', 'Recycling')]
    quantity  = models.IntegerField(null=True, blank=True)
    wastehandling  = models.CharField(
        max_length=255, choices=choices, blank=True, null=True)
    wasteHandlingLocation  = models.CharField(
        max_length=255, blank=True, null=True)
    photographs  = models.ImageField(null=True, blank=True)
    documents  = models.FileField(null=True, blank=True)
    remarks  = models.CharField(max_length=255, null=True, blank=True)



class MaterialSourcing(Baseclass):
    # materialsourcing_id = models.ForeignKey(
    #     EnvMonitoring, related_name="MaterialSourcing", on_delete=models.CASCADE, null=True, blank=True)
    _materialChoices = [('Material A', 'Material A'), ('Material B', 'Material B'), ('Material C', 'Material C'), ('Material D', 'Material D')]
    typeOfMaterial = models.CharField(max_length=255, choices=_materialChoices ,  null=True, blank=True)
    source = [('Mines', 'Mines'), ('Blast', 'Blast')]
    approvals  = models.FileField(null=True , blank= True )
    sourceOfQuarry  = models.CharField(max_length=255, choices=source ,  null=True, blank=True)

    # def __str__(self) -> str:
    #     return self.materialsourcing_id.env_monitoring.email