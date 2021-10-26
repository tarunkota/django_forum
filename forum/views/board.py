from ..models import Board
from ..serializers import BoardSerializer
from rest_framework import generics
from rest_framework import permissions
from .utils import IsAdminOrReadOnly

from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse,HttpResponse


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

class BoardView(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    lookup_field="slug"



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def joinBoard(request,slug):
    """
    """
    board = Board.objects.get(slug=slug)
    if(board.subscribers.all().filter(user= request.user).exists()):
        board.subscribers.remove(request.user.profile)
        board.save()
    else:
        board.subscribers.add(request.user.profile)
        board.save()
    return JsonResponse({"msg":"success"})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSubscribedBoards(request):
    """
    """
    boards = Board.objects.filter(subscribers=request.user.profile).all()
    data = BoardSerializer(boards,many=True).data
    return JsonResponse(data,safe=False)


@api_view(['GET'])
def exploreBoards(request):
    """
    """
    boards = Board.objects.filter().all()
    boards2 = Board.objects.filter().order_by('-pk')
    data={}
    data['popular'] = BoardSerializer(boards,many=True).data
    data['new'] = BoardSerializer(boards2,many=True).data
    return JsonResponse(data,safe=False)