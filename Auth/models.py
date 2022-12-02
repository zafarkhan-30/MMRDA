
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin , PermissionManager
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


class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    # username = models.CharField(max_length=255)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)

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


# class report(models.Model):
#     report = models.FileField(upload_to='reports/', max_length=254)


# # # Abstarct Baseclass for EnvMonitoring for common field
# class Baseclass(models.Model):
#     choices = [('JAN-MAR 2022', 'JAN-MAR 2022'), ('APR-JUN 2022',
#                                                   'APR-JUN 2022'), ('JULY-AUG 2022', 'JULY-AUG 2022')]
#     quarter = models.CharField(
#         max_length=255, choices=choices, null=True, blank=True)
#     package_choice = [('CA-08', 'CA-08'), ('CA-09', 'CA-09'), ('CA-10', 'CA-10'),
#                       ('CA-11', 'CA-11'), ('CA-12', 'CA-12'), ('CA-54', 'CA-54')]
#     package = models.CharField(
#         max_length=255, choices=package_choice,  null=True, blank=True)
#     location = models.PointField(null=True, blank=True)
#     date = models.DateField(auto_now=True, null=True, blank=True)

#     class Meta:
#         abstract = True


# # --------------------------------------OCCUPATINOL HEALTH & SAFTEY MODEL-----------------------------------

# class occupationalHealthSafety(models.Model):
#     user = models.ForeignKey(
#         User, related_name="occupationalHealthSafety", on_delete=models.CASCADE)
#     location = models.PointField(null=True, blank=True)
#     joining_medical_check = models.BooleanField()
#     accidental_check = models.BooleanField()
#     nature_of_accident = models.CharField(
#         max_length=255, null=True, blank=True)
#     date_of_incident = models.DateField(auto_now_add=True, null=True, blank=True)
#     collective_majors = models.CharField(max_length=255, null=True, blank=True)
#     incident_reporting = models.CharField(
#         max_length=255, null=True,  blank=True)
#     type_of_incident = models.CharField(max_length=255, null=True, blank=True)
#     barricading = models.BooleanField()
#     photographs = models.ImageField(
#         upload_to='photographs/', null=True, blank=True)

#     def __str__(self) -> str:
#         return self.user.email


# # ----------------------- TRANINING MODEL ---------------------------------------------------------


