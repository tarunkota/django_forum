import json
from ..models import Post,SavedPost,Profile,Board,PollResult
from ..serializers import PostSerializer,ProfileSerializer1
from rest_framework import generics
from rest_framework import permissions
from .utils import IsOwnerOrReadOnly
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse,HttpResponse
from .feed import loadPostsInCache



class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field="slug"

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile,board = self.request.POST.get('id'))


class PostView(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field="slug"



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPost(request):
    """
    """
    profile = request.user.profile
    d=json.loads(request.body)
    post = Post(profile=profile,board = Board.objects.get(id = d['board']))

    if('title' in d):
        post.title = d['title']
    if('text' in d):
        post.text = d['text']

    if('media' in d):
        post.media = d['media']
        post.postType = Post.FILE

    if('question' in d):
        post.question = d['question']
        post.postType = Post.QUESTION

    if('poll' in d):
        post.question = d['poll']
        post.postType = Post.POLL

    if('optionA' in d):
        post.optionA = d['optionA']
    if('optionB' in d):
        post.optionB = d['optionB']
    if('optionC' in d):
        post.optionC = d['optionC']
    if('optionD' in d):
        post.optionD = d['optionD']
    if('solution' in d):
        post.solution = d['solution']
    if('correctOption' in d):
        post.correctOption = d['correctOption']

    post.save()
    print(post)
    loadPostsInCache(post.board.slug)
    loadPostsInCache("")
    return JsonResponse({"msg":"success"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def upvotePost(request,slug):
    """
    """
    post = Post.objects.get(slug=slug)
    if(not post.upvoted_by.all().filter(user = request.user).exists()):
        post.upvoted_by.add(request.user.profile)
        post.downvoted_by.remove(request.user.profile)
        post.save()
    else:
        post.upvoted_by.remove(request.user.profile)
        post.save()
    return JsonResponse({"msg":"success"})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def downvotePost(request,slug):
    """
    """
    post = Post.objects.get(slug=slug)
    if(not post.downvoted_by.all().filter(user= request.user).exists()):
        post.upvoted_by.remove(request.user.profile)
        post.downvoted_by.add(request.user.profile)
        post.save()
    else:
        post.downvoted_by.remove(request.user.profile)
        post.save()
    return JsonResponse({"msg":"success"})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def savePost(request,slug):
    """
    """
    post = Post.objects.get(slug=slug)
    if(not SavedPost.objects.filter(profile=request.user.profile,post=post).exists()):
        s = SavedPost(post=post,profile=request.user.profile)
        s.save()
    else:
        SavedPost.objects.filter(profile=request.user.profile,post=post).all().delete()
    return JsonResponse({"msg":"success"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def voteboxPost(request,slug):
    """
    """
    post = Post.objects.get(slug=slug)
    data = {}
    data["upvoted"] = post.upvoted_by.filter(user=request.user).exists()
    data["downvoted"] = post.downvoted_by.filter(user=request.user).exists()
    data["joined"] = post.board.subscribers.filter(user=request.user).exists()
    data["saved"] = SavedPost.objects.filter(post=post,profile=request.user.profile).exists()

    return JsonResponse(data)


@api_view(['GET'])
def userPosts(request,username):
    """
    """
    profile = Profile.objects.get(username=username)
    posts = Post.objects.filter(profile=profile).order_by('-score')[0:10]
    likedPosts = Post.objects.filter(upvoted_by=profile).order_by('-score')[0:10]
    data ={}
    data['posts']= PostSerializer(posts,many=True).data
    data['liked_posts'] = PostSerializer(likedPosts,many=True).data
    data['profile'] = ProfileSerializer1(profile,many=False).data

    return JsonResponse(data,safe=False)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def votePoll(request,slug):
    """
    """
    post = Post.objects.get(slug=slug)
    profile  = request.user.profile
    pr,cc = PollResult.objects.get_or_create(profile=profile,post=post)
    d=json.loads(request.body)
    pr.result = d['result']
    pr.save()
    return JsonResponse({"msg":"success"})



@api_view(['GET'])
def postsUpdate(request):
	for post in Post.objects.all():
		post.save()
	return JsonResponse({"msg":"success"})



