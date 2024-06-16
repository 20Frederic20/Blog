from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Autorise seulement le propriétaire de l'objet à le modifier.
    """
    def has_object_permission(self, request, view, obj):
        # Les utilisateurs authentifiés peuvent lire les objets.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Les propriétaires des objets peuvent les modifier.
        return obj.owner == request.user
    

class ReadOnly(BasePermission):
    """
    Autorise seulement les méthodes GET, HEAD et OPTIONS.
    """
    def has_permission(self, request, view):
        return request.method in ['GET', 'HEAD', 'OPTIONS']

class WriteOnly(BasePermission):
    """
    Autorise seulement les méthodes POST, PUT et DELETE.
    """
    def has_permission(self, request, view):
        return request.method in ['POST', 'PUT', 'DELETE']