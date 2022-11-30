from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group



# from django.contrib.auth.mixins import PermissionRequiredMixin
# class MyView(PermissionRequiredMixin,):
# 	permission_required = ('polls.can_open', 'polls.can_edit')





# class StaffPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_staff


# class Allpermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_mmrda and request.user.is_kfw and request.user.is_consultant and  request.user.is_contractor



# class MMRDApermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_mmrda 

# class KFWpermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_kfw


# class consultantPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_consultant

# class contractorPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_contractor



# def _is_in_group(user,group_name):

# 	"""
# 	This function takes user and group as parameter and returns true if the user is present in that group
# 	"""

# 	try:
# 		return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
# 	except Group.DoesNotExist as e:
# 		return None


# def _has_group_permission(user,required_group):

# 	"""
# 	This function takes the user and checks if the user is in the list of groups
# 	"""

# 	return any([_is_in_group(user,group_name) for group_name in required_group])


# class IsMMRDA(BasePermission):

# 	required_group=["mmrda"]
    

# 	def has_permission(self,request,view):
# 		has_group_permission=_has_group_permission(request.user,self.required_group)
# 		return request.user and has_group_permission