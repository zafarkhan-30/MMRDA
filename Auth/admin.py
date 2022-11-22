from django.contrib import admin
from .models import (User , report ,photographs)
# Register your models here.


admin.site.register(User)
admin.site.register(report)
# #admin.site.register(project_issue)
# admin.site.register(traning)
# # admin.site.register(occupationalHealthSafety)
admin.site.register(photographs)
