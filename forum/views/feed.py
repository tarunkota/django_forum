from ..models import Post,Board
from ..serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes



@api_view(['GET'])
def feed(request):
	slug = request.GET.get("board","")
	if(slug==""):
		#order by score
		feed = Post.objects.filter(active=True).order_by('-score')[0:10]
		
	else:
		board = Board.objects.get(slug=slug)
		feed = Post.objects.filter(board=board).filter(active=True).order_by('-score')[0:10]

	data = PostSerializer(feed,many=True).data
	return JsonResponse(data,safe=False)
