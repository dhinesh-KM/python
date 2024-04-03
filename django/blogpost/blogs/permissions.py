from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

        
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the object has a 'user' attribute.
        #if hasattr(obj, 'author'):
        #    print("************",obj.author, request.user)
            # Check if the request user is the owner of the object.
        return obj.author == request.user

        return False
        # Instance must have an attribute named `author`.
        #return obj.author == request.user
    
class IsUserOrReadOnly(permissions.BasePermission):

        
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the object has a 'user' attribute.
        if hasattr(obj, 'user'):
            # Check if the request user is the owner of the object.
            return obj.user == request.user

        return False

        # Instance must have an attribute named `author`.
        #return obj.user == request.user
   
    