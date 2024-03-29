import json
from ..models import Comment,Post
from ..serializers import CommentSerializer
from rest_framework import generics
from rest_framework import permissions
from .utils import IsOwnerOrReadOnly
from django.http import JsonResponse

from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse


class CreateComment(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field="uid"

    def perform_create(self, serializer):
        # get the post / comment too here
        serializer.save(user=[self.request.user])


class CommentView(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer()
    lookup_field="uid"




@api_view(['GET'])
def postComments(request,slug):

    #order by score
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post).filter(reply=None).order_by('created')
    data = CommentSerializer(comments,many=True).data
    return JsonResponse(data,safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createComment(request):
    """
    Create comments on post
    """
    d = json.loads(request.body)
    profile = request.user.profile
    post = Post.objects.get(slug=d['slug'])

    c = Comment(post = post,profile=profile,text=d['text'])



    if('cuid' in d):
        if(d['cuid']!=""):
            c.reply = Comment.objects.get(uid=d["cuid"])


    c.save()

    return JsonResponse({"msg":"success"},safe=False)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def upvoteComment(request,uid):
    """
    """
    comment = Comment.objects.get(uid=uid)
    if(not comment.upvoted_by.all().filter(user = request.user).exists()):
        comment.upvoted_by.add(request.user.profile)
        comment.downvoted_by.remove(request.user.profile)
        comment.save()
    else:
        comment.upvoted_by.remove(request.user.profile)
        comment.save()
    return JsonResponse({"msg":"success"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def downvoteComment(request,uid):
    """
    """
    comment = Comment.objects.get(uid=uid)
    if(not comment.downvoted_by.all().filter(user = request.user).exists()):
        comment.upvoted_by.remove(request.user.profile)
        comment.downvoted_by.add(request.user.profile)
        comment.save()
    else:
        comment.downvoted_by.remove(request.user.profile)
        comment.save()
    return JsonResponse({"msg":"success"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def voteboxComment(request,uid):
    """
    """
    comment = Comment.objects.get(uid=uid)
    data = {}
    data["upvoted"] = comment.upvoted_by.filter(user=request.user).exists()
    data["downvoted"] = comment.downvoted_by.filter(user=request.user).exists()

    return JsonResponse(data)