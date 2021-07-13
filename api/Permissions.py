from rest_framework.permissions import BasePermission, SAFE_METHODS

class AuthorityToMakeRequestForAParticularBusiness(BasePermission):
    message= "Making a request for this buiness is restricted to owner only"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.business == request.user.id
