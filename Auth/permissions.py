from rest_framework.permissions import BasePermission


class StaffPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class Allpermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mmrda and request.user.is_kfw and request.user.is_consultant and  request.user.is_contractor



class MMRDApermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mmrda 

class KFWpermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_kfw


class consultantPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_consultant

class contractorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_contractor