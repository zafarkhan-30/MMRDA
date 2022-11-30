from django.contrib import admin
from .models import (User ,)
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# class UserAdminConfig(UserAdmin):
#     model = User
  
#     # list_display = ('email', 'is_staff', 'is_active',)
#     # list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password', 'username',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
    

#         ('Group Permissions', {
#              ('groups', 'user_permissions', )
#         })),


admin.site.register(User)
# admin.site.register(report)
# admin.site.register(GroupManager)
# # #admin.site.register(project_issue)
# # admin.site.register(traning)
# # # admin.site.register(occupationalHealthSafety)
# admin.site.register(photographs)
