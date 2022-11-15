from django.contrib import admin
from .models import (User , Air , Noise , water , report , EnvMonitoring , EnvQualityMonitoring , photographs)
# Register your models here.


admin.site.register(User)
admin.site.register(report)
admin.site.register(Air)
admin.site.register(water)
admin.site.register(Noise)
admin.site.register(EnvMonitoring)
admin.site.register(EnvQualityMonitoring)
# admin.site.register(social_Monitoring)
# admin.site.register(PAP)
# admin.site.register(Rehabilation)
# #admin.site.register(project_issue)
# admin.site.register(traning)
# # admin.site.register(occupationalHealthSafety)
admin.site.register(photographs)
