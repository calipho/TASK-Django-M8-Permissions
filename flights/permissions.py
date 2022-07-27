import datetime
from email import message
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class HasAuthority(BasePermission):
    message = "You do not have authority to do this."

    def has_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_staff


class IsTrueAfterCancel(BasePermission):
    message = "You can't cancel this booking only after 3 days"

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            if obj.date < datetime.date.today() + datetime.timedelta(days=3):
                return False
            return True
        return True
