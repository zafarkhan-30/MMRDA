
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



# # Abstarct Baseclass for EnvMonitoring for common field
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
    location= models.PointField(null=True, blank=True)
    date = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True



# --------------------------------------OCCUPATINOL HEALTH & SAFTEY MODEL-----------------------------------

class occupationalHealthSafety(models.Model):
    user = models.ForeignKey(
        User, related_name="occupationalHealthSafety", on_delete=models.CASCADE)
    # nature = [('')]
    nature_of_accident = models.CharField(
        max_length=255, null=True, blank=True)
    medical_check = models.BooleanField()
    accidental_check = models.BooleanField()
    incident_issuer = models.BooleanField()
    date_of_incoident = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    barricading = models.BooleanField()
    photographs = models.ImageField(
        upload_to='photographs/', null=True, blank=True)

    def __str__(self) -> str:
        return self.user.email


# # ----------------------- TRANINING MODEL ---------------------------------------------------------

class traning(models.Model):

    traning_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True, blank=True)
    traning_title = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    no_of_attends = models.IntegerField(null=True, blank=True)
    male = models.CharField(max_length=255, null=True, blank=True)
    female = models.CharField(max_length=255, null=True, blank=True)
    incharge_person = models.CharField(max_length=253, null=True, blank=True)
    initiated_by = [('GC (Genral Contractor)', 'GC (Genral Contractor)'),
                    ('Consultant', 'Consultant'), ('MMRDA', 'MMRDA')]
    traninig_initiated_by = models.CharField(
        max_length=255, choices=initiated_by, null=True, blank=True)
    conduct_date = models.DateField(auto_now=True, null=True, blank=True)
    traning_date = models.DateField(auto_now=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    photographs = models.ImageField(
        upload_to='traning_photographs/', null=True, blank=True)

    def __str__(self) -> str:
        return self.traning_id.email

# # -----------------------------PHOTOGRAPHS MODEL ----------------------------------------


class photographs(models.Model):

    site_name = models.CharField(max_length=255, null=True, blank=True)
    incharge_person = models.CharField(max_length=244, null=True, blank=True)
    photographs_clcik_by = models.CharField(
        max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, null=True, blank=True)
    site_photographs = models.ImageField(
        upload_to='site_photographs/', null=True, blank=True)
