from ..models import Profile
from ..serializers import ProfileSerializer1
from rest_framework import generics
from rest_framework import permissions
from .utils import IsOwnerOrReadOnly



class Profile(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer1
    lookup_field = 'username'
