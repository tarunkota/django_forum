from ..models import Comment
from ..serializers import CommentSerializer
from rest_framework import generics
from rest_framework import permissions
from .utils import IsOwnerOrReadOnly

class CreateComment(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field="uid"

    def perform_create(self, serializer):
        # get the post / comment too here
        serializer.save(user=[self.request.user])


class Comment(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field="uid"
