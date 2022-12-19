from django.db import models
from Auth.models import User
from django.db.models.signals import post_save
from django.contrib.gis.db import models
from django.utils import timezone
# Create your models here.

# ----------------------------------SOCIAL MONITORING MODLES----------------------------------------

class Baseclass(models.Model):
    choices = [('Jan-Mar 2022', 'Jan-Mar 2022'), ('Apr-Jun 2022',
                                                  'Apr-Jun 2022'), ('July-Aug 2022', 'July-Aug 2022')]
    quarter = models.CharField(
        max_length=255, choices=choices, null=True, blank=True)
    package_choice = [('CA-08', 'CA-08'), ('CA-09', 'CA-09'), ('CA-10', 'CA-10'),
                      ('CA-11', 'CA-11'), ('CA-12', 'CA-12'), ('CA-54', 'CA-54')]
    packages= models.CharField(
        max_length=255, choices=package_choice,  null=True, blank=True)
    # latitude = models.IntegerField(null=True, blank=True)
    # longitude = models.IntegerField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    dateOfConduct = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True




class PAP(Baseclass):
    # pap_id = models.ForeignKey(
    #     social_Monitoring, related_name='PAPs', on_delete=models.CASCADE)
    # quarter = None
    # package = None
    # date    = None
    dateOfNotification = models.DateField(null=True, blank=True)
    actions = [('Agreed for rehabilitation', 'Agreed for rehabilitation'),
               ('Agreed For compensation', 'Agreed For compensation'),
               ('Not agreed', 'Not agreed')]
    actionTaken = models.CharField(
        max_length=100, choices=actions, null=True, blank=True)
    # Compensation_offered_type = [('Alternate accommodation / Commercial Unit', 'Alternate accommodation / Commercial Unit'),
    #                              ('Cash compensation', 'Cash compensation'), ('Land Provided Area', 'Land Provided Area')]
    # compensationStatus = models.CharField(
    #     max_length=255, choices=Compensation_offered_type, null=True, blank=True)
    _eligibilityChoices = [('Yes', 'Yes'), ('No', 'No')]
    eligibility = models.CharField(max_length= 255 ,choices= _eligibilityChoices,  null= True , blank=True)      
    type_of_pap = [
        ('individual', 'individual'), ('commercial', 'commercial'),
        ('land', 'land'), ('Institutional', 'Institutional'),
        ('other', 'other')]
    categoryOfPap = models.CharField(
        max_length=255, choices=type_of_pap, null=True, blank=True)
    Ownership_status_choices = [
        ('structure', 'structure'), ('land', 'land'), ('Both', 'Both')]
    ownershipStatus = models.CharField(
        max_length=255, choices=Ownership_status_choices, null=True, blank=True)
    status = [
        ('legal', 'legal'),
        ('under dispute', 'under dispute'),
        ('illegal', 'illegal')]
    legalStatus = models.CharField(
        max_length=255, choices=status, null=True, blank=True)
    rehabilitationStatusChoices = [('YES', 'YES'), ('NO', 'NO')]
    rehabilitationStatus  = models.CharField( max_length=255, choices= rehabilitationStatusChoices , blank = True , null =True  )
    isShiftingAllowance = models.BooleanField(blank =True)
    isLivelihoodSupport = models.CharField(
        max_length=255, null=True, blank=True)
    isTraining = models.BooleanField(blank= True )
    isTenaments = models.BooleanField(blank =True)
    isTransportationAllowance = models.BooleanField(blank =True)
    isfinancialSupport = models.BooleanField(blank =True)
    isCommunityEngagement = models.BooleanField(blank =True )
    isEngagementType = models.CharField(
        max_length=255, null=True, blank=True)
    CompensationStatusChoises = [('Cash Compensation' , 'Cash Compensation'),('Land Provided Area' , 'Land Provided Area') ,
    ('Alternate accommodation / Commercial Unit' , 'Alternate accommodation / Commercial Unit')]
    compensationStatus = models.CharField(max_length=255, choices=CompensationStatusChoises,null=True, blank=True )
    # isAccommodation = models.FileField(
    #     null=True, blank=True)
    # isCashCompensation = models.CharField(max_length=255, null=True, blank=True)
    # isLandProvided = models.CharField(
    #     max_length=255, null=True, blank=True)



# Agreed For rehabilation
class Rehabilation(models.Model):
    PAP_id = models.OneToOneField(
        PAP, related_name='rehabilation', on_delete=models.CASCADE)
    shifting_allowance = models.BooleanField(blank =True)
    livelihood_support = models.CharField(
        max_length=255, null=True, blank=True)
    traning = models.BooleanField(blank= True )
    tenaments = models.BooleanField(blank =True)
    transport_allowance = models.BooleanField(blank =True)
    additional_financial_support_or_revolving_fund = models.BooleanField()
    Community_engagement = models.CharField(
        max_length=255, null=True, blank=True)

    
# Compensation Offered Type


class Compensation(models.Model):
    PAP_id = models.OneToOneField(
        PAP, related_name="Compensation", on_delete=models.CASCADE)
    Alternate_accommodation_or_Commercial_Unit = models.FileField(
        null=True, blank=True)
    cash_compensation = models.CharField(max_length=255, null=True, blank=True)
    land_provided_area = models.CharField(
        max_length=255, null=True, blank=True)


# Labour  Camp Model ----------------------------------------------

class LabourCamp(Baseclass):
    LabourCampTitle = models.CharField(max_length=255, null=True, blank=True)
    transportationFacility = models.BooleanField(blank=True, null = True)
    isToilet = models.BooleanField(blank =True)
    isDrinkingWater = models.BooleanField(blank =True)
    isDemarkingOfPathways = models.BooleanField(blank =True)
    isSignagesLabeling = models.BooleanField(blank =True)
    isRegularHealthCheckup = models.BooleanField(blank= True )
    isAvailabilityOfDoctor = models.BooleanField(   blank =True)
    isFirstAidKit = models.BooleanField( blank =True)
    isKitchenArea = models.BooleanField(blank =True)
    isFireExecution = models.BooleanField(blank =True)
    isSegregationOfWaste = models.BooleanField(blank =True)
    isRoomsOrDoms = models.BooleanField(blank=True)


#     camp_id = models.ForeignKey(
#         social_Monitoring, related_name='labour_camp', on_delete=models.CASCADE)
#     # transport_facility = models.BooleanField(blank=True)

#     def __str__(self):
#         return self.camp_id.sm_id.email


# def create_data(sender, instance, **kwargs):
#     if kwargs['created']:
#         created = LabourCamp.objects.create(camp_id=instance)
# post_save.connect(create_data, sender=social_Monitoring)


class ConstructionSiteDetails(Baseclass):
    
    # labourCamp_id = models.ForeignKey(
    #     LabourCamp, related_name='constructioncamp', on_delete=models.CASCADE)
    # # quarter =None
    sitephotographs = models.ImageField(upload_to='site_photographs/' , null=True, blank=True)
    isDemarkingOfPathwaysCheck = models.BooleanField(blank = True)
    isSignagesLabelingCheck = models.BooleanField(blank= True )
    isRegularHealthCheckup = models.BooleanField(default=False)
    isAvailabilityOfDoctor = models.BooleanField(default=False)
    isFirstAidKit = models.BooleanField(default=False)
    isDrinkingWaterCheck  = models.BooleanField(blank =True)
    isToiletFacility = models.BooleanField( blank =True)
    

    

# class LabourCampDetails(Baseclass):
#     labourcamp_id = models.ForeignKey(
#         LabourCamp, related_name='labourcampdetails', on_delete=models.CASCADE )
#     quarter = None
#     package = None
#     date = None
#     toilets = models.BooleanField(blank =True)
#     Drinking_water = models.BooleanField(blank =True)
#     demarking_of_pathways = models.BooleanField(blank =True)
#     signAges_or_labeling = models.BooleanField(blank =True)
#     Regular_Health_Checkup = models.BooleanField(blank= True )
#     Availability_Of_Doctor = models.BooleanField(   blank =True)
#     Availability_Of_First_aid_Kit = models.BooleanField( blank =True)
#     kitchen_area = models.BooleanField(blank =True)
#     fire_execution = models.BooleanField(blank =True)
#     segregation_of_waste = models.BooleanField(blank =True)
#     rooms_or_doms = models.CharField(max_length=255, null=True, blank=True)



# class Test(Baseclass):
#     location = None 
#     longitude = models.CharField(max_length=255, null=True, blank=True)
#     latitude = models.CharField(max_length=255, null=True)
    