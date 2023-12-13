from rest_framework import permissions

class IsTeacherOfAdminSchool(permissions.BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.is_staff:
            return request.user.school_id == request.user.school_id
        return False