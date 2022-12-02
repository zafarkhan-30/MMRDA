from django.contrib import admin 
from .models import (User ,)
from django.contrib.auth.admin import UserAdmin  
# Register your models here.

admin.site.register(User)
# admin.site.register(report)
# admin.site.register(GroupManager)
# # #admin.site.register(project_issue)
# # admin.site.register(traning)
# # # admin.site.register(occupationalHealthSafety)
# admin.site.register(photographs)
