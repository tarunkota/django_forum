from ..models import Board
from ..serializers import BoardSerializer
from rest_framework import generics
from rest_framework import permissions
from .utils import IsAdminOrReadOnly


class CreateBoard(generics.CreateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    lookup_field="slug"
    
    def perform_create(self, serializer):
        serializer.save(admins=[self.request.user])

class Board(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    lookup_field="slug"
