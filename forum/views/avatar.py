from ..models import Avatar
from ..serializers import AvatarSerializer
from rest_framework import generics
from rest_framework import permissions
from .utils import IsOwnerOrReadOnly




class Avatar(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    lookup_field = "profile__username"
