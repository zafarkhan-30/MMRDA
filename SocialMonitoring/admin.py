from django.contrib import admin
from .models import (PAP, social_Monitoring, Rehabilation, LabourCamp,Compensation,
                     ConstructionSiteDetails, LabourCampDetails)
# Register your models here.


admin.site.register(social_Monitoring)
admin.site.register(PAP)
admin.site.register(Rehabilation)
admin.site.register(LabourCamp)
admin.site.register(ConstructionSiteDetails)
admin.site.register(Compensation)
admin.site.register(LabourCampDetails)
