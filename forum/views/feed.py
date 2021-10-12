from ..models import Post,Board
from ..serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes


from django.core.cache import cache



def loadPostsInCache(slug):
	if(slug==""):
		feed = Post.objects.filter(active=True).order_by('-score')[0:10]
	else:
		board = Board.objects.get(slug=slug)
		feed = Post.objects.filter(board=board).filter(active=True).order_by('-score')[0:10]
	data = PostSerializer(feed,many=True).data	
	cache.set('feed_'+slug,data,None)


def getFeed(slug):
	dataCache = cache.get('feed_'+slug)
	if(dataCache==None):
		loadPostsInCache(slug)
		dataCache = cache.get('feed_'+slug)
	return dataCache



@api_view(['GET'])
def feed(request):
	slug = request.GET.get("board","")
	data = getFeed(slug)
	return JsonResponse(data,safe=False)



@api_view(['GET'])
def feedReload(request):
	loadPostsInCache("")
	for board in Board.objects.all():
		loadPostsInCache(board.slug)
	return JsonResponse({"msg":"success"})
