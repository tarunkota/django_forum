from ..models import Post
from ..serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions
from .utils import IsOwnerOrReadOnly

class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field="slug"

    def perform_create(self, serializer):
        serializer.save(user=[self.request.user])


class Post(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field="slug"
