
# Register your models here.

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active' , 'is_mmrda' , 'is_kfw' , 'is_consultant' , 'is_contractor' ,'groups' , 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)

# admin.site.register(report)
# admin.site.register(GroupManager)
# # #admin.site.register(project_issue)
# # admin.site.register(traning)
# # # admin.site.register(occupationalHealthSafety)
# admin.site.register(photographs)
