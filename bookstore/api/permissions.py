
"""
Permissions to allow only adult in Book list and detail
"""
from rest_framework.permissions import BasePermission

class IsAdult(BasePermission):
    def has_permission(self, request, view):
        """
        if user.age < 18 return False, True else
        """
        if request.user.age < 18 :
            return False
        return True
    

    
