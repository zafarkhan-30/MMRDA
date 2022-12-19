from django.contrib import admin
from .models import (PAP, Rehabilation, LabourCamp,Compensation, 
                     ConstructionSiteDetails)
# Register your models here.


# admin.site.register(social_Monitoring)
admin.site.register(PAP)
admin.site.register(Rehabilation)
admin.site.register(LabourCamp)
admin.site.register(ConstructionSiteDetails)
admin.site.register(Compensation)
# admin.site.register(Test)
# admin.site.register(LabourCampDetails)
