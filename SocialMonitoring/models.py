from django.db import models
from Auth.models import User
from django.db.models.signals import post_save
from django.contrib.gis.db import models
from django.utils import timezone

# Create your models here.
# ----------------------------------SOCIAL MONITORING MODLES----------------------------------------

class Baseclass(models.Model):
    choices = [('JAN-MAR 2022', 'JAN-MAR 2022'), ('APR-JUN 2022',
                                                  'APR-JUN 2022'), ('JULY-AUG 2022', 'JULY-AUG 2022')]
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


class social_Monitoring(models.Model):
    sm_id = models.ForeignKey(
        User, related_name='social_monitoring', on_delete=models.CASCADE)

    def __str__(self):
        return self.sm_id.email


def create_data(sender, instance, **kwargs):
    if kwargs['created']:
        created = social_Monitoring.objects.create(sm_id=instance)
post_save.connect(create_data, sender=User)


class PAP(Baseclass):
    pap_id = models.ForeignKey(
        social_Monitoring, related_name='PAPs', on_delete=models.CASCADE)
    date_of_notification =models.DateTimeField(auto_now_add=True, null=True, blank=True)
    actions = [('Agreed for rehabilation', 'Agreed for rehabilation'),
               ('Agreed For Compensation', 'Agreed For Compensation'),
               ('Not agreed', 'Not agreed')]
    action_taken = models.CharField(
        max_length=100, choices=actions, null=True, blank=True)
    Compensation_offered_type = [('Alternate accommodation / Commercial Unit', 'Alternate accommodation / Commercial Unit'),
                                 ('Cash Compensation', 'Cash compensation'), ('Land Provided Area', 'Land Provided Area')]
    Compensation_offered = models.CharField(
        max_length=255, choices=Compensation_offered_type, null=True, blank=True)
    eligibility_status = models.BooleanField()
    type_of_pap = [
        ('individual', 'individual'),
        ('commercial', 'commercial'),
        ('land', 'land'),
        ('Institutional', 'Institutional'),
        ('other', 'other')]
    category_of_PAP = models.CharField(
        max_length=255, choices=type_of_pap, null=True, blank=True)
    Ownership_status_choices = [
        ('structure', 'structure'), ('land', 'land'), ('Both', 'Both')]
    Ownership_status = models.CharField(
        max_length=255, choices=Ownership_status_choices, null=True, blank=True)
    status = [
        ('legal', 'legal'),
        ('under dispute', 'under dispute'),
        ('illegal', 'illegal')]
    legal_status = models.CharField(
        max_length=255, choices=status, null=True, blank=True)

    def __str__(self) -> str:
        return self.pap_id.sm_id.email

 # Agreed For rehabilation


class Rehabilation(models.Model):
    rehabilation_id = models.OneToOneField(
        PAP,related_name= 'rehabilation' , on_delete=models.CASCADE)
    shifting_allowance = models.BooleanField()
    livelihood_support = models.CharField(
        max_length=255, null=True, blank=True)
    traning = models.BooleanField()
    tenaments = models.BooleanField()
    transport_allowance = models.BooleanField()
    additional_financial_support_or_revolving_fund = models.BooleanField()
    Community_engagement = models.CharField(
        max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.rehabilation_id.pap_id.sm_id.email

# Compensation Offered Type


class Compensation(models.Model):
    Compensation_id = models.OneToOneField(
        PAP, related_name="Compensation", on_delete=models.CASCADE)
    Alternate_accommodation_or_Commercial_Unit = models.FileField(
        null=True, blank=True)
    cash_compensation = models.CharField(max_length=255, null=True, blank=True)
    land_provided_area = models.CharField(
        max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.Compensation_id.pap_id.sm_id.email


# Labour  Camp Model ----------------------------------------------


class LabourCamp(Baseclass):
    camp_id = models.ForeignKey(
        social_Monitoring, related_name='labour_camp', on_delete=models.CASCADE)
    transport_facility = models.BooleanField()

def create_data(sender, instance, **kwargs):
    if kwargs['created']:
        created = LabourCamp.objects.create(camp_id=instance)
post_save.connect(create_data, sender=social_Monitoring)


class ConstructionSiteDetails(Baseclass):
    construction_id = models.ForeignKey(
        LabourCamp, related_name='constructioncamp', on_delete=models.CASCADE)
    site_photographs = models.ImageField(null=True, blank=True)
    demarking_of_pathways = models.BooleanField()
    signAges_or_labeling = models.BooleanField()
    # medical_choices = [('Regular Health Checkup', 'Regular Health Checkup'),
    #                    ('Availability Of Doctor', 'Availability Of Doctor'),
    #                    ('Availability Of First aid Kit', 'Availability Of Firstaid Kit')]
    # Medical_facility = models.CharField(
    #     max_length=255, choices=medical_choices)
    Regular_Health_Checkup = models.BooleanField(default=False)
    Availability_Of_Doctor = models.BooleanField(default=False)
    Availability_Of_First_aid_Kit = models.BooleanField(default=False)
    Drinking_water = models.BooleanField()
    Toilet_facility = models.BooleanField()


class LabourCampDetails(Baseclass):
    labourcamp_id = models.ForeignKey(
        LabourCamp, related_name='labourcampdetails', on_delete=models.CASCADE)
    toilets = models.BooleanField()
    Drinking_water = models.BooleanField()
    demarking_of_pathways = models.BooleanField()
    signAges_or_labeling = models.BooleanField()
    # medical_choices = [('Regular Health Checkup', 'Regular Health Checkup'),
    #                    ('Availability Of Doctor', 'Availability Of Doctor'),
    #                    ('Availability Of First aid Kit', 'Availability Of Firstaid Kit')]
    # Medical_facility = models.CharField(
    #     max_length=255, choices=medical_choices, null=True, blank=True)
    Regular_Health_Checkup = models.BooleanField(default=False)
    Availability_Of_Doctor = models.BooleanField(default=False)
    Availability_Of_First_aid_Kit = models.BooleanField(default=False)

    kitchen_area = models.BooleanField()
    fire_execution = models.BooleanField()
    segregation_of_waste = models.BooleanField()
    rooms_or_doms = models.CharField(max_length=255, null=True, blank=True)
