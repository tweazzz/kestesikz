from rest_framework import permissions

class IsAdminOfSchool(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.admin.school == obj.school