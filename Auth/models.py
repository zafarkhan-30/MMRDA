
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.gis.db import models
from django.db.models.signals import post_save
# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_active, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError("email cannot be empty")
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser,
                          date_joined=now, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_mmrda = models.BooleanField(default=False)
    is_kfw = models.BooleanField(default=False)
    is_consultant = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class report(models.Model):
    report = models.FileField(upload_to='reports/', max_length=254)


# ------------------------------- ENV MONITORING MODEL----------------------------------------

class EnvMonitoring(models.Model):
    env_quality_monitoring = models.ForeignKey(
        User, related_name="Quality_Monitoring", on_delete=models.CASCADE)
    choices = [('CA-07' , 'CA-07'),('CA-10' , 'CA-10'),('CA-09' , 'CA-09')]
    package = models.CharField(max_length= 255 , choices=choices)

    def __str__(self) -> str:
        return self.env_quality_monitoring.email




class EnvQualityMonitoring(models.Model):
    eqm_id = models.ForeignKey(
        EnvMonitoring, related_name='EnvQualityMonitoring', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.eqm_id.env_quality_monitoring.email

def create_data(sender, instance ,**kwargs):                                                                    
        if kwargs['created']:
            created  = EnvQualityMonitoring.objects.create(eqm_id = instance)
post_save.connect(create_data, sender=EnvMonitoring)


# Abstarct Baseclass for EnvMonitoring for common field
class Baseclass(models.Model):
    quarter = models.CharField(max_length=255)
    package = models.CharField(max_length=255)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    date = models.DateField(auto_now= True )

    class Meta:
        abstract = True


class Air(Baseclass):
    air_id = models.ForeignKey(
        EnvQualityMonitoring, on_delete=models.CASCADE)
    standard = models.FloatField(max_length=255)
    deviation = models.FloatField(max_length=255)
    trends = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "filled By :- " + self.air_id.eqm_id.env_quality_monitoring.email


class water(Baseclass):
    water_id = models.ForeignKey(
        EnvQualityMonitoring, on_delete=models.CASCADE)
    # Water = [('GroundWater', 'Ground Water'), ('SeaWater', 'Sea Water'), ]
    quality_of_water = models.CharField(max_length=255)
    source_of_water = models.CharField(max_length=255)

    def __str__(self) -> str:
        return "filled By :- " + self.water_id.eqm_id.env_quality_monitoring.email


class Noise(Baseclass):
    noise_id = models.ForeignKey(
        EnvQualityMonitoring, on_delete=models.CASCADE)
    details = models.CharField(max_length=255)

    def __str__(self) -> str:
        return "filled By :- " + self.noise_id.eqm_id.env_quality_monitoring.email


# class TreeManagment(Baseclass):
#     tree_id = models.ForeignKey(
# 	    EnvMonitoring, related_name='EnvironmentalMonitoring', on_delete=models.CASCADE)
#     planted = models.BooleanField()
#     planted_details = models.CharField(max_length=255)
#     No_of_trees_cut = models.IntegerField()
#     Cutting_details = models.CharField(max_length=255)
#     transplanted = models.BooleanField()
#     transplanted_details = models.CharField(max_length=255)
#     Management = models.CharField(max_length=255)


# class WasteTreatments(Baseclass):
# 	waste_id = models.ForeignKey(
# 	    EnvMonitoring, related_name="waste_treatments", on_delete=models.CASCADE)
# 	_type = [('Hazardous Waste', 'Hazardous'), ('Bio Waste', 'Bio'),
# 	          ('electronic waste', 'Electronic'), ]
# 	waste_type = models.CharField(max_length=255, choices=_type)
# 	quantity = models.IntegerField()
# 	package = models.CharField(max_length=255)
# 	photographs = models.ImageField(null=True)
# 	documents = models.FileField(null=True)
# 	remarks = models.CharField(max_length = 255)
    


# class MaterialSourcing(Baseclass):
# 	materialsourcing_id = models.ForeignKey(EnvMonitoring , related_name = "MaterialSourcing" , on_delete = models.CASCADE)
# 	source = [('Mines', 'Mines'),('Blast', 'Blast')]
# 	approvals = models.FileField(null=True)
# 	source_of_quary = models.CharField(max_length=255, choices=source)


# class RegulatoryCompliance(models.Model):
#     pass


# # ----------------------------------SOCIAL MONITORING MODLES----------------------------------------

# class social_Monitoring(models.Model):
#     sm_id = models.ForeignKey(
#         User, related_name='social_monitoring', on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.sm_id.email


# class PAP(Baseclass):

#     pap_id = models.ForeignKey(social_Monitoring, on_delete=models.CASCADE)
#     identification = models.FileField(max_length=255)
#     date_of_identification = models.DateField(auto_now=True)
#     compensation = models.CharField(max_length=255)
#     type_of_pap = [
#         ('individual', 'individual'),
#         ('commercial', 'commercial'),
#         ('land', 'land'),
#         ('religious', 'religious'),
#         ('other', 'other')
#     ]
#     type = models.CharField(max_length=255, choices=type_of_pap)
#     legal_satus = [
#         ('legal', 'legal'),
#         ('under dispute', 'under dispute'),
#         ('illegal', 'illegal')
#     ]
#     status = models.CharField(max_length=255, choices=legal_satus)

#     offerd_type = [
#         ('alternate accommodation', 'alternate accommodation'),
#         ('cash compensation', 'cash compensation'),
#         ('land provided area', 'land provided area')
#     ]
#     compensation_offered = models.CharField(max_length=255, choices=offerd_type)

#     def __str__(self) -> str:
#         return self.pap_id.sm_id.email


# class Rehabilation(models.Model):
#     rehabilation_id = models.OneToOneField(PAP, on_delete=models.CASCADE)
#     shifting_allowance = models.CharField(max_length=255)
#     livelihood = models.CharField(max_length=255)
#     traning = models.BooleanField()
#     tenements = models.BooleanField()

#     def __str__(self) -> str:
#         return self.rehabilation_id.pap_id.sm_id.email

# class LabourCamp(Baseclass):
# 	transport_facility = models.BooleanField()



# class constructionCamp(Baseclass):
# 	camp_id = models.ForeignKey(LabourCamp , on_delete = models.CASCADE)
# 	site_photographs = models.ImageField(null = True)
# 	Drinking_water = models.BooleanField()
# 	Toilet_facility = models.BooleanField()


# class LabourSite(Baseclass):
# 	laboursite_id = models.ForeignKey(LabourCamp , on_delete = models.CASCADE)
# 	toilets = models.BooleanField()
# 	Drinking_water = models.BooleanField()
# 	kitchen_area = models.BooleanField()
# 	fire_execution = models.BooleanField()
# 	waste_segragation = models.BooleanField()\

# # --------------------------------------OCCUPATINOL HEALTH & SAFTEY MODEL-----------------------------------

# # class occupationalHealthSafety(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     nature_of_accident = models.CharField(max_length=255)
# #     medical_check = models.BooleanField()
# #     accidental_check = models.BooleanField()
# #     incident_issuer = models.BooleanField()
# #     date_of_incoident = models.DateTimeField(auto_now_add=True)
# #     barricading = models.BooleanField()
# #     photographs = models.ImageField(upload_to='photographs/', null=True)

# #     def __str__(self) -> str:
# #         return self.user.email


# # ----------------------- PROJECT ISSUE MODEL ----------------------------------------------------------

# # class project_issue(models.Model):
# #     raise_by = [
# #         ('consulatnt', 'consulatnt'),
# #         ('contractor', 'contractor'),
# #     ]
# #     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
# #     Name = models.CharField(max_length=255, choices=raise_by)
# #     description = models.CharField(max_length=255)
# #     date = models.DateField(auto_now_add=True)
# #     location = models.CharField(max_length=255)

# #     def __str__(self) -> str:
# #         return "issue raised by :-" + self.user_id.email


# # ----------------------- TRANINING MODEL ---------------------------------------------------------

# class traning(models.Model):

#     traning_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     no_of_attends = models.IntegerField()
#     incharge_person = models.CharField(max_length=253)
#     conduct_date = models.DateField(auto_now=True)
#     traning_date = models.DateField(auto_now=True)
#     description = models.CharField(max_length=255)
#     photographs = models.ImageField(upload_to='traning_photographs/', null=True)
#     # locations = models.PointField()

#     def __str__(self) -> str:
#         return self.traning_id.email

# # -----------------------------PHOTOGRAPHS MODEL ----------------------------------------


class photographs(models.Model):

    site_name = models.CharField(max_length=255)
#     incharge_person = models.CharField(max_length=244)
#     photographs_clcik_by = models.CharField(max_length=100)
#     date = models.DateTimeField(auto_now=True)
#     site_photographs = models.ImageField(upload_to='site_photographs/', null=False)
