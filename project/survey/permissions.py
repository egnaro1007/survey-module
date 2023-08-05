from rest_framework.permissions import BasePermission


class Anyone(BasePermission):
    def has_permission(self, request, view):
        return True


class CanViewResponses(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.permission in ['god', 'admin', 'manager']


class CanManageSurvey(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.permission in ['god', 'admin', 'manager']


class CanManageUser(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.permission in ['god', 'admin']


class CanManageAdmin(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.permission in ['god']
