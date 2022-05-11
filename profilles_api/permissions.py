from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to update their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check if a user is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
        

class UpdateOwnFeed(permissions.BasePermission):
    """Allow users to update their own status/feed"""
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id